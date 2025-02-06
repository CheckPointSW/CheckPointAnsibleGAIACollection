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
module: cp_gaia_snmp_trap_receiver
author: Ameer Asli (@chkp-ameera)
description:
- Change the SNMP trap receiver configuration.
short_description: Change the SNMP trap receiver configuration.
version_added: '6.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  address:
    description: Receiver address.
    required: True
    type: str
  ver:
    description:
      - Receiver version.
    type: str
    choices: [v1, v2, v3]
  community_string:
    description:
      - Receiver community - Required only in case of v1/v2 versions
      - Trap Community String used by the trap receiver to determine which traps are accepted from a device.
    type: str
"""

EXAMPLES = """
- name: Set community string for SNMP trap receiver
  check_point.gaia.cp_gaia_snmp_trap_receiver:
    community_string: some_string
    address: trap_receiver_address
"""

RETURN = """
snmp_trap_receiver:
  description: The updated trap receiver details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        address=dict(type='str', required=True),
        ver=dict(type='str', choices=['v1', 'v2', 'v3']),
        community_string=dict(type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'snmp-trap-receiver'
    ignore = []
    show_params = ["address"]

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
