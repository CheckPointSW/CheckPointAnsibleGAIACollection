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
module: cp_gaia_snmp_user
author: Ameer Asli (@chkp-ameera)
description:
- Change a SNMPv3 USM user's characteristics.
short_description: Change a SNMPv3 USM user's characteristics.
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
    description: SNMPv3 USM user name.
    required: True
    type: str
  permission:
    description:
      - User permission.
    type: str
    choices: [read-only, read-write]
  allowed_virtual_systems:
    description:
      - Configured Virtual Devices allowed for the USM user - vsid range 0-512.
    type: str
  authentication:
    description:
      - Authentication details.
    type: dict
    suboptions:
        protocol:
            description:
              - Authentication protocol, MD5 and SHA1 are not supported starting from R81.
            type: str
            choices: [MD5, SHA1, SHA256, SHA512]
        password:
            description:
              - Authentication Password - (8 or more printable characters, Limited by 128 characters)
              - Each SNMPv3 USM user must have an authentication pass phrase.
            type: str
        password_hash:
            description:
              - Authentication Hashed Password - (8 or more printable characters, Limited by 128 characters)
              - Each SNMPv3 USM user must have an authentication pass phrase.
            type: str
  privacy:
    description:
      - Privacy details.
    type: dict
    suboptions:
        protocol:
            description:
              - Privacy protocol.
            type: str
            choices: [AES, DES, AES256]
        password:
            description:
              - Privacy Password - (8 or more printable characters, Limited by 128 characters)
              - An SNMPv3 USM user with a privacy security level must have a privacy pass phrase.
            type: str
        password_hash:
            description:
              - Privacy Hashed Password - (8 or more printable characters, Limited by 128 characters)
              - An SNMPv3 USM user with a privacy security level must have a privacy pass phrase.
            type: str
"""

EXAMPLES = """
- name: Set permission field for the snmp user
  check_point.gaia.cp_snmp_gaia_user:
    permission: read-only
    name: snmpuser
"""

RETURN = """
snmp_user:
  description: The updated user details.
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
        permission=dict(type='str', required=False, choices=['read-only', 'read-write']),
        allowed_virtual_systems=dict(type='str', required=False),
        authentication=dict(
            type="dict",
            options=dict(
                protocol=dict(type="str", required=False, choices=['MD5', 'SHA1', 'SHA256', 'SHA512']),
                password=dict(type="str", required=False, no_log=True),
                password_hash=dict(type="str", required=False, no_log=True)
            )
        ),
        privacy=dict(
            type="dict",
            options=dict(
                protocol=dict(type="str", required=False, choices=['AES', 'DES', 'AES256']),
                password=dict(type="str", required=False, no_log=True),
                password_hash=dict(type="str", required=False, no_log=True)
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'snmp-user'
    ignore = []
    show_params = ["name"]

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
