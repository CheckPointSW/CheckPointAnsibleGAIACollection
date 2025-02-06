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
author: Roi Tal (@chkp-roital)
description: Add, modify or delete Secruity Groups.
module: cp_gaia_maestro_security_groups
short_description: Add, modify or delete Secruity Groups.
version_added: "7.0.0"
requirements: ['supported starting from gaia_api >= 1.8']
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
  id:
    description: Security Group ID. If not specified, all other fields are required (except description ans sites) as a new SG will be created.
    required: False
    type: int
  interfaces:
    description: Orchestrator ports that will be assigned to this Security Group. At least one of 'id' or 'interface-name' parameters must be provided.
    required: False
    type: list
    elements: dict
    suboptions:
      id:
        description: Interface ID (e.g. "1/13/1")
        required: False
        type: str
      name:
        description: Interface name (e.g. "eth1-05")
        required: False
        type: str
      description:
        description: Description of the interface
        required: False
        type: str
  gateways:
    description: Maestro Gateways that will be assigned to this Security Group.
    required: False
    type: list
    elements: dict
    suboptions:
      id:
        description: Maestro Gateway ID (serial number)
        type: str
      description:
        description: Description of this Maestro Gateway
        required: False
        type: str
  sites:
    description:
      - Security Group Site descriptions. The security group is assigned to 'sites' automatically
      - according to gateways associated with the Security Group.
    required: False
    type: list
    elements: dict
    suboptions:
      id:
        description: ID of this site
        type: int
      description:
        description: Description of this site
        type: str
  ftw_configuration:
    description: First time wizard configuration for this Security Group
    required: False
    type: dict
    suboptions:
      hostname:
        description: Hostname for Security Group
        type: str
      is_vsx:
        description: Determines if this Security Group is a VSX
        type: bool
      one_time_password:
        description: One time password for Secure Internal Communication (SIC)
        type: str
      admin_password:
        description: Admin password for Security Group
        type: str
  mgmt_connectivity:
    description: The IP addresses that will be used to manage this Security Group
    required: False
    type: dict
    suboptions:
      ipv4_address:
        description: IPv4 address for Security Group
        type: str
      ipv4_mask_length:
        description: IPv4 mask length for Security Group
        type: int
      default_gateway:
        description: Default Gateway address for Security Group
        type: str
  description:
    description: Security Group description
    required: False
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int

notes:
- Supports C(check_mode).
"""

EXAMPLES = """
- name: Change GWs of SG1
  check_point.gaia.cp_gaia_security_groups:
    id: 1
    gateways: [{id: 1007RT1992}]

- name: Create new end-to-end SG
  check_point.gaia.cp_gaia_maestro_security_groups:
    interfaces: [{"name": "eth1-Mgmt1"}]
    gateways: [{"id": "3112ET1966"}]
    ftw_configuration: {"hostname": "New_SG", "is_vsx": false, "one_time_password": "otpotp", "admin_password": "adminpassword"}
    mgmt_connectivity: {"ipv4_address": "1.1.1.1", "ipv4_mask_length": 24, "default_gateway": "1.1.1.4"}
"""

RETURN = """
maestro_security_group:
  description: The updated MSecurity Group details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        id=dict(type='int'),
        interfaces=dict(
            type="list", elements="dict",
            options=dict(
                name=dict(type="str"),
                id=dict(type="str"),
                description=dict(type="str")
            )
        ),
        gateways=dict(
            type="list", elements="dict",
            options=dict(
                id=dict(type="str"),
                description=dict(type="str")
            )
        ),
        sites=dict(
            type="list", elements="dict",
            options=dict(
                id=dict(type="int"),
                description=dict(type="str")
            )
        ),
        ftw_configuration=dict(
            type="dict",
            options=dict(
                hostname=dict(type="str"),
                is_vsx=dict(type="bool"),
                one_time_password=dict(type="str", no_log=True),
                admin_password=dict(type="str", no_log=True)
            )
        ),
        mgmt_connectivity=dict(
            type="dict",
            options=dict(
                ipv4_address=dict(type="str"),
                ipv4_mask_length=dict(type="int"),
                default_gateway=dict(type="str")
            )
        ),
        description=dict(type="str")
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'maestro-security-group'
    show_params = ["id"]
    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
