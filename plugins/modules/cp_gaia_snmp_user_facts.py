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
module: cp_gaia_snmp_user_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show the SNMPv3 USM users currently configured.
short_description: Show SNMPv3 USM user/s.
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
  name:
    description: SNMPv3 USM user name to show. If not specified, all users information is returned.
    required: false
    type: str
"""

EXAMPLES = """
- name: Show SNMP users
  check_point.gaia.cp_gaia_snmp_user_facts:

- name: Show SNMPv3 USM user by specifying it's name
  check_point.gaia.cp_gaia_snmp_user_facts:
    name: snmpuser
"""

RETURN = """
ansible_facts:
    description: The SNMPv3 USM user/s facts.
    returned: always.
    type: dict
    contains:
        objects:
            description:
              - List of SNMP users.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description:
                      - SNMPv3 USM User name.
                    returned: always
                    type: str
                permission:
                    description:
                      - User permission.
                    returned: always
                    type: str
                allowed_virtual_systems:
                    description:
                      - Configured Virtual Devices allowed for the USM user - vsid range 0-512.
                    returned: always
                    type: str
                authentication:
                    description:
                      - Authentication details.
                    returned: always
                    type: dict
                    contains:
                        protocol:
                            description:
                              - Authentication protocol, MD5 and SHA1 are not supported starting from R81.
                            returned: always
                            type: str
                privacy:
                    description:
                      - Privacy details.
                    returned: always
                    type: dict
                    contains:
                        protocol:
                            description:
                              - Privacy protocol.
                            returned: always
                            type: str
                data_privacy:
                    description:
                      - Related to AutoPriv/AutnNoPriv in SecurityLevel in the RFC. True- AutoPriv ,False- AuthNoPriv.
                    returned: always
                    type: bool
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type="str", required=False)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "snmp-user"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
