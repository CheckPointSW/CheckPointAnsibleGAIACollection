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
- Show Config Point parameters by full path or prefix.
- To see the parameters documentation go to https://<IP>/param_docs/ on the Gaia machine.
module: cp_gaia_param_facts
short_description: Show Config Point parameters.
version_added: '7.1.0'
notes:
- Supports C(check_mode).
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
  param_path:
    description: Parameter full path or prefix, for example C(security-gateway.DLP).
    required: True
    type: str
  filter_by:
    description:
      - Show only parameters matching the filter, in the format C(<filter_type>=true).
      - The filter type can be one of C(modified), C(with-comments) or C(not-default), for example C(modified=true).
    required: False
    type: str
  member_id:
    description: SMO member ID of the member to show the data from. Default is the ID of the current login member.
    required: False
    type: int
  wait_for_task:
    description: Wait for task or return immediately.
    required: False
    default: True
    type: bool
"""


EXAMPLES = """
- name: Show all DLP parameters
  check_point.gaia.cp_gaia_param_facts:
    param_path: security-gateway.DLP

- name: Show only the DLP parameters that were modified
  check_point.gaia.cp_gaia_param_facts:
    param_path: security-gateway.DLP
    filter_by: modified=true
"""


RETURN = """
show_param:
  description:
    - The task result of the show-param request.
    - The matching parameters are in C(tasks[0].task-details[0].param-list), each with its
      name, current-value, default-value, description, comments, pending and last-modified.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async


def main():
    # arguments for the module:
    fields = dict(
        param_path=dict(type='str', required=True),
        filter_by=dict(type='str'),
        member_id=dict(type='int')
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    # this API accepts the Virtual System ID only as a string
    fields['virtual_system_id'] = dict(type='str', required=False)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'show-param'

    res = chkp_api_operation(module, api_call_object)

    # this action does not change system configuration
    res['changed'] = False

    module.exit_json(**res)


if __name__ == "__main__":
    main()
