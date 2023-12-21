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
author: Roi Tal (@chkp-roital)
description:
- Show Maestro Security Groups topology.
module: cp_gaia_maestro_security_groups_facts
options:
  include_pending_changes:
    description: If true, show pending topology, as opposed to the one actually deployed
    required: False
    default: False
    type: bool
  id:
    description: ID of Security Group to show. If not specified, all Security Groups information is returned
    required: False
    type: int
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
short_description:Show Maestro Security Groups topology.
version_added: '7.0.0'
notes:
- Supports C(check_mode).

"""

EXAMPLES = """
- name: Show current information of Security Group 1
  check_point.gaia.cp_gaia_maestro_security_groups_facts:
      id: 1
      include_pending_changes: false

"""

RETURN = """
ansible_facts:
    description: The Maestro Security Group/s facts.
    returned: always.
    type: dict
    contains:
        security_groups:
            description:
              - List of Security Groups.
            returned: always
            type: list
            elements: dict
            contains:
                id:
                    description:
                      - Security Group ID.
                    returned: always
                    type: int
                interfaces:
                    description:
                      - The interfaces that are assigned to the Security Group.
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        id:
                            description:
                              - Port ID.
                            returned: always
                            type: str
                        interface_name:
                            description:
                              - Interface name.
                            returned: always
                            type: str
                        description:
                            description:
                              - Description of this interface.
                            returned: always
                            type: str
                        vlans:
                            description:
                              - VLANs this interface belongs to
                            returned: always
                            type: list
                            elements: str
                gateways:
                    description:
                      - The Maestro Gateways that are assigned to the Security Group.
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        id:
                            description:
                              - Maestro Gateway ID.
                            returned: always
                            type: str
                        site:
                            description:
                              - Site this Gateway belongs to.
                            returned: always
                            type: int
                        security_group:
                            description:
                              - The Security Group this Gateway belongs to.
                            returned: always
                            type: int
                        member_id:
                            description:
                              - The member ID of this Gateway, if it's assigned to a Security Group.
                            returned: always
                            type: int
                        model:
                            description:
                              - Model of this Gateway.
                            returned: always
                            type: str
                        version:
                            description:
                              - OS version installed on this Gateway.
                            returned: always
                            type: dict
                            contains:
                                major:
                                    description:
                                      - Major version
                                    returned: always
                                    type: str
                        downlink_ports:
                            description:
                              - The Orchestrator ports which are connected to the Gateway.
                            returned: always
                            type: list
                            elements: dict
                            contains:
                                orchestrator_id: 
                                    description:
                                      - ID of the Orchestrator to which this port belongs
                                    returned: always
                                    type: str
                                port:
                                    description:
                                      - Port ID
                                    returned: always
                                    type: str
                        description:
                            description:
                              - Description of this Gateway.
                            returned: always
                            type: str
                        state:
                            description:
                              - State of this Gateway.
                            returned: always
                            type: str
                        weight:
                            description:
                              - Weight assigned to this Gateway, in case it's assigned to a Security Group.
                            returned: always
                            type: int
                sites:
                    description:
                      - List of site descriptions in this Security Group context
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        id:
                            description:
                              - ID of this site
                            returned: always
                            type: int
                        description:
                            description:
                              - Description of this site
                            returned: always
                            type: str
                ftw_configuration:
                    description:
                      - First time wizard configuration for this Security Group
                    returned: always
                    type: dict
                    contains:
                        hostname:
                            description: Hostname of this Security Group
                            returned: always
                            type: str
                        is_vsx:
                            description: Is this Security Group a VSX
                            returned: always
                            type: bool
                        one_time_password:
                            description: One time password of Secure Internal Communication (SIC)
                            returned: always
                            type: str
                        admin_password:
                            description: Admin password od Security Group
                            returned: always
                            type: str
                mgmt_connectivity:
                    description: 
                      - The IP addresses that will be used to manage this Security Group
                    returned: always
                    type: dict 
                    contains:
                        ipv4_address:
                            description: IPv4 address of this Security Group
                            returned: always
                            type: str
                        ipv4_mask_length:
                            description: IPv4 mask length for Security Group
                            returned: always
                            type: int
                        default_gateway:
                            description: Default Gateway address for Security Group
                            returned: always
                            type: str
                description:
                    description:
                      - Description of this Security Group.
                    returned: always
                    type: str

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        include_pending_changes=dict(required=False, type='bool'),
        id=dict(required=False, type='int')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "maestro-security-group"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
