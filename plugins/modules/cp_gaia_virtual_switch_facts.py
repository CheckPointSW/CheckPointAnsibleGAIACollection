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
module: cp_gaia_virtual_switch_facts
short_description: Get virtual-switch objects facts on Check Point over Web Services API
description:
  - Get virtual-switch objects facts on Check Point devices.
  - All operations are performed over Web Services API.
  - This module handles both operations, get a specific object and get several objects,
    For getting a specific object use the parameter 'id' to specify the virtual switch id.
version_added: "6.0.0"
author: Omer Hadad (@chkp-omerhad)
options:
  id:
    description:
      - Virtual Switch ID.
        This parameter is relevant only for getting a specific Virtual Switch object.
    type: str

"""
EXAMPLES = """
- name: show-virtual-switch
  cp_gaia_virtual_switch_facts:
    id: 1
- name: show-virtual-switches
  cp_gaia_virtual_switch_facts:
"""
RETURN = """
ansible_facts:
  description: The checkpoint object facts.
  returned: always.
  type: dict
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all

def run_module():
    fields = dict(
        id=dict(type="int"),
        member_id=dict(type="int")
        )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    if module.params["id"]:
        api_call_object = 'virtual-switch'
    else:
        api_call_object = 'virtual-switches'
    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(**res)
def main():
    run_module()
if __name__ == '__main__':
    main()
