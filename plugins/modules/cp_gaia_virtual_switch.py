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
---
module: cp_gaia_virtual_switch
short_description: Manages virtual switch on Check Point Gateway over Web Services API
description:
  - Manages virtual switches on Check Point gateways, including creating, updating, and removing virtual switches.
  - All operations are performed over the Web Services API.
version_added: "6.0.0"
author: Omer Hadad (@chkp-omerhad)
options:
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  version:
    description: Gaia API version for example 1.8.
    required: False
    type: str
  wait_for_task:
    description: Wait for task or return immediately.
    required: False
    default: True
    type: bool
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
  id:
    description:
      - Virtual Switch ID.
      - This parameter is used to change an existing virtual switch or create a new one if it does not exist.
    type: str
  name:
    description:
      - Name of the virtual switch.
      - This parameter is used to change an existing virtual switch or create a new one if it does not exist.
    type: str
  interfaces:
      description:
      - Collection of interfaces to be set, identified by their names. Replaces existing interfaces.
      type: list
      elements: dict
      suboptions:
        name:
          description: Interface name.
          type: str
"""
EXAMPLES = """
- name: set virtual switch
  check_point.gaia.cp_gaia_virtual_switch:
    id: 10
    name: AnsibleSwitch
    interfaces:
      - name: eth1-01
      - name: eth2.300
      - name: bond1.20
"""
RETURN = """
cp_gaia_virtual_switch:
  description: virtual switch creation output.
  returned: always.
  type: dict
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import (
    chkp_api_call,
    checkpoint_argument_spec_for_all,
    checkpoint_argument_spec_for_async,
)


def run_module():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        id=dict(type='str'),
        name=dict(type='str'),
        interfaces=dict(type='list', elements='dict', options=dict(name=dict(type='str')))
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    ignore = ['status']
    show_params = ['id']
    add_params = {'name': module.params['name'], 'id': module.params['id']}
    api_call_object = 'virtual-switch'
    res = chkp_api_call(module, api_call_object, True, ignore=ignore, show_params=show_params, add_params=add_params)
    module.exit_json(**res)


def main():
    run_module()


if __name__ == '__main__':
    main()
