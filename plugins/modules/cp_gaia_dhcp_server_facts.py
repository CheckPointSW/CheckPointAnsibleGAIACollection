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
author: Ameer Asli (@chkp-ameera)
description:
- Shows DHCP server information.
module: cp_gaia_dhcp_server_facts
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
short_description: Shows DHCP server information.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
"""


EXAMPLES = """
- name: Shows DHCP server information.
  check_point.gaia.cp_gaia_dhcp_server_facts:
"""


RETURN = """
ansible_facts:
    description: The interface/s facts.
    returned: always.
    type: dict
    contains:
        enabled:
            description: DHCP server status.
            returned: always
            type: bool
        subnets:
            description: Subnets.
            returned: always
            type: list
            elements: dict
            contains:
                subnet:
                    description: IPv4 address for the subnet.
                    returned: always
                    type: str
                max_lease:
                    description: The longest lease that the server can allocate, in seconds.
                    returned: always
                    type: int
                default_lease:
                    description: The default lease that the server allocates, in seconds.
                    returned: always
                    type: int
                enabled:
                    description: Enable DHCP on this subnet.
                    returned: always
                    type: bool
                ip_pools:
                    description: Range of IPv4 addresses that the server assigns to hosts.
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        start:
                            description: The first IPv4 address of the range.
                            returned: always
                            type: str
                        include:
                            description: Specifies whether to include or exclude this range of IPv4 addresses in the IP pool.
                            returned: always
                            type: str
                        end:
                            description: The last IPv4 address of the range.
                            returned: always
                            type: str
                        enabled:
                            description: Enables or disables the DHCP Server for this subnet IP pool.
                            returned: always
                            type: bool
                netmask:
                    description: Subnet mask.
                    returned: always
                    type: int
                default_gateway:
                    description: The IPv4 address of the default gateway for the DHCP clients.
                    returned: always
                    type: str
                virtual_system_id:
                    description: Virtual System ID.
                    returned: always
                    type: int
                dns:
                    description: DNS configuration.
                    returned: always
                    type: dict
                    contains:
                            domain_name:
                                description: Domain name.
                                returned: always
                                type: str
                            primary:
                                description: The IPv4 address of the Primary DNS server for the DHCP clients.
                                returned: always
                                type: str
                            secondary:
                                description: The IPv4 address of the Secondary DNS server for the DHCP clients
                                             (to use if the primary DNS server does not respond).
                                returned: always
                                type: str
                            tertiary:
                                description: The IPv4 address of the Tertiary DNS server for the DHCP clients
                                             (to use if the primary and secondary DNS servers do not respond).
                                returned: always
                                type: str
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        virtual_system_id=dict(type="int", required=False)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    api_call_object = 'dhcp-server'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
