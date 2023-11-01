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
author: Ophir Khill (@chkp-ophirk)
description:
- getting information of a chosen dynamic layer.
module: cp_gaia_dynamic_content_layer_facts
options:
    version:
        description: Gaia API version for example 1.6.
        required: False
        type: str
    name:
        description: dynamic layer to show
        required: true
        type: str
    wait_for_task:
        description: Wait for task or return immediately.
        required: False
        default: True
        type: bool
short_description: getting information of the chosen dynamic layer.
version_added: '5.1.0'

"""

EXAMPLES = """
- name: show dynamic layer
  check_point.gaia.cp_gaia_dynamic_content_layer_facts:
    name: dynamic_layer
"""

RETURN = """
layer_summary:
  description: the details of the installed policy on the requested layer
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type='str', required=True)
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'show-dynamic-layer'

    res = chkp_api_operation(module, api_call_object)

    # this action does not change system configuration
    res['changed'] = False

    module.exit_json(**res)


if __name__ == "__main__":
    main()
