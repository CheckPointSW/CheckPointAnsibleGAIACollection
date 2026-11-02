#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = """
author: Ameer Asli (@chkp-ameera)
description:
- Set Config Point parameters.
- To see the parameters documentation go to https://<IP>/param_docs/ on the Gaia machine.
module: cp_gaia_param
short_description: Set Config Point parameters.
version_added: '7.1.0'
notes:
- Supports C(check_mode). In check mode the request is sent with C(dry_run), so nothing is saved.
requirements:
- supported starting from gaia_api >= 1.8
- supported on Gaia versions R82 and above
options:
  version:
    description: Gaia API version for example 1.8.
    required: False
    type: str
  virtual_system_id:
    description: VSX Virtual System ID which presents the context switch.
    required: False
    type: str
  param_list:
    description: List of parameters to be set.
    required: True
    type: list
    elements: dict
    suboptions:
      param_path:
        description: Parameter full path.
        required: True
        type: str
      value:
        description:
          - Parameter value, can be a string, int, boolean, object or a list of them.
          - Can not be used together with I(use_default).
        type: raw
      comments:
        description: Comments to be added to the parameter, length is limited to 256 characters.
        type: str
      use_default:
        description:
          - Set the parameter back to its default value.
          - Can not be used together with I(value).
        type: bool
      volatile:
        description: Set the parameter with the value specified until the next reboot.
        type: bool
      virtual_system_id:
        description: VSX Virtual System IDs to set the parameter in, can be C(all) or specific IDs, for example C(2,4,7-10).
        type: str
  dry_run:
    description: Run the request without saving to the database, return only the values that would change.
    required: False
    default: False
    type: bool
  use_regex:
    description: Indicates that I(param_path) includes C(*).
    required: False
    default: False
    type: bool
  wait_for_task:
    description: Wait for task or return immediately.
    required: False
    default: True
    type: bool
"""


EXAMPLES = """
- name: Set a parameter value and return another one to its default
  check_point.gaia.cp_gaia_param:
    param_list:
      - param_path: gaia.infra.httpd.cp_httpd_configuration.children_core_dumps
        value: true
        comments: enabled for debugging purpose
      - param_path: gaia.infra.rest_api.gunicorn.timeout
        use_default: true

- name: Check which parameters would change, without saving
  check_point.gaia.cp_gaia_param:
    param_list:
      - param_path: gaia.infra.httpd.cp_httpd_configuration.children_core_dumps
        value: true
    dry_run: true
"""


RETURN = """
set_param:
  description: The task result of the set-param request, including the parameters that were set.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async


# check if any of the parameters has changed
def has_changed(result):
    try:
        details = result['set_param']['tasks'][0]['task-details'][0]
    except (KeyError, IndexError, TypeError):
        # no task details (wait_for_task is false), assume a change
        return True

    if 'changed-params' in details:
        return details['changed-params'] > 0
    return any(param.get('value-changed') for param in details.get('param-list', []))


def main():
    # arguments for the module:
    fields = dict(
        param_list=dict(type='list', elements='dict', required=True, options=dict(
            param_path=dict(type='str', required=True),
            value=dict(type='raw'),
            comments=dict(type='str'),
            use_default=dict(type='bool'),
            volatile=dict(type='bool'),
            virtual_system_id=dict(type='str')
        ), mutually_exclusive=[['value', 'use_default']]),
        dry_run=dict(type='bool', default=False),
        use_regex=dict(type='bool', default=False)
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    # this API accepts the Virtual System ID only as a string
    fields['virtual_system_id'] = dict(type='str', required=False)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-param'

    # check mode uses the API's own dry run, so nothing is saved
    if module.check_mode:
        module.params['dry_run'] = True

    res = chkp_api_operation(module, api_call_object, read_only=module.check_mode)
    res['changed'] = has_changed(res)

    module.exit_json(**res)


if __name__ == "__main__":
    main()
