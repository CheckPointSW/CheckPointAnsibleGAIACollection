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
module: cp_gaia_snmp_custom_trap
author: Ameer Asli (@chkp-ameera)
description:
- Change the SNMP custom_trap configuration.
short_description: Change the SNMP custom_trap configuration.
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
  name:
    description: Custom trap name.
    required: True
    type: str
  oid:
    description:
      - OID (object identifier).
    type: str
  operator:
    description:
      - Comparison operator.
    type: str
    choices: [equal, not-equal, less-than, greater-than, changed]
  threshold:
    description:
      - The value you want to compare to.
    type: raw
  frequency:
    description:
      - Polling interval in seconds.
    type: int
  msg:
    description:
      - Custom trap message.
    type: str
"""

EXAMPLES = """
- name: Set threshold for custom trap
  check_point.gaia.cp_gaia_snmp_custom_trap:
    threshold: 12
    name: custom_trap_name
"""

RETURN = """
snmp_custom_trap:
  description: The updated custom trap details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(type='str', required=True),
        oid=dict(type='str'),
        operator=dict(type='str', choices=['equal', 'not-equal', 'less-than', 'greater-than', 'changed']),
        threshold=dict(type='raw'),
        frequency=dict(type='int'),
        msg=dict(type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'snmp-custom-trap'
    ignore = []
    show_params = ["name"]

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
