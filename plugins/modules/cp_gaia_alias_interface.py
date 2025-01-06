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
module: cp_gaia_alias_interface
author: Duane Toler (@duanetoler)
description:
- Modify alias interface.
short_description: Modify alias interface.
version_added: '8.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  name:
    description: Interface name with format "<parent interface>:<id>", for example  eth0:1, eth0:2 .. etc.
    required: true
    type: str
  ipv4_address:
      description: Interface IPv4 address.
      required: false
      type: str
  ipv4_mask_length:
      description: Interface IPv4 address mask length.
      required: false
      type: int
"""

EXAMPLES = """
- name: Set comment field of a alias interface
  check_point.gaia.cp_gaia_alias_interface:
    comments: "eth0:1 interface"
    name: eth0:1
"""

RETURN = """
alias_interface:
  description: The updated interface details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(required=True, type='str'),
        ipv4_address=dict(required=True, type='str'),
        ipv4_mask_length=dict(required=True, type='int')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'alias-interface'
    ignore = ['parent']
    show_params = ['name']
    add_params = {}
    parent_and_id = module.params["name"].split(":")
    if len(parent_and_id) == 2:
        add_params = {"parent": parent_and_id[0] }

    res = chkp_api_call(module, api_call_object, True, ignore=ignore, show_params=show_params, add_params=add_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()