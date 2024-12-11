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
- Change DHCP server settings.
module: cp_gaia_dhcp_server
short_description: Change DHCP server settings.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  enabled:
        description: DHCP server status.
        required: False
        type: bool
  subnets:
        description: Subnets.
        required: False
        type: list
        elements: dict
        suboptions:
            subnet:
                description: IPv4 address for the subnet.
                required: False
                type: str
            max_lease:
                description: The longest lease that the server can allocate, in seconds.
                required: False
                type: int
                default: 86400
            default_lease:
                description: The default lease that the server allocates, in seconds.
                required: False
                type: int
                default: 43200
            enabled:
                description: Enable DHCP on this subnet.
                required: False
                type: bool
            ip_pools:
                description: Range of IPv4 addresses that the server assigns to hosts.
                required: False
                type: list
                elements: dict
                suboptions:
                    start:
                        description: The first IPv4 address of the range.
                        required: False
                        type: str
                    include:
                        description: Specifies whether to include or exclude this range of IPv4 addresses in the IP pool.
                        required: False
                        type: str
                        choices: ['include', 'exclude']
                    end:
                        description: The last IPv4 address of the range.
                        required: False
                        type: str
                    enabled:
                        description: Enables or disables the DHCP Server for this subnet IP pool.
                        required: False
                        type: bool
            netmask:
                description: Subnet mask.
                required: False
                type: int
            default_gateway:
                description: The IPv4 address of the default gateway for the DHCP clients.
                required: False
                type: str
            virtual_system_id:
                description: Virtual System ID.
                required: False
                type: int
            dns:
                description: DNS configuration.
                required: False
                type: dict
                suboptions:
                        domain_name:
                            description: Domain name.
                            required: False
                            type: str
                        primary:
                            description: The IPv4 address of the Primary DNS server for the DHCP clients.
                            required: False
                            type: str
                        secondary:
                            description: The IPv4 address of the Secondary DNS server for the DHCP clients
                                         (to use if the primary DNS server does not respond).
                            required: False
                            type: str
                        tertiary:
                            description: The IPv4 address of the Tertiary DNS server for the DHCP clients
                                         (to use if the primary and secondary DNS servers do not respond).
                            required: False
                            type: str
"""


EXAMPLES = """
- name: Change DHCP server settings
  check_point.gaia.cp_gaia_dhcp_server:
    enabled: False
    subnets: [
        {"subnet": "4.5.6.0",
        "netmask": 24,
        "max_lease": 86400,
        "default_lease": 43200,
        "default_gateway": "4.5.6.1",
        "ip_pools": [{"start": "4.5.6.5", "end": "4.5.6.7", "enabled": True, "include": "include"}],
        "dns": {"domain_name": "my_domain_name", "primary": "8.8.8.8", "secondary": "8.8.8.8", "tertiary": "8.8.4.4"},
        "enabled": True, virtual_system_id: 0}
    ]
"""


RETURN = """
dhcp_server:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type='bool'),
        virtual_system_id=dict(type='int', required=False),
        subnets=dict(
            type='list', elements='dict',
            options=dict(
                subnet=dict(type='str'),
                max_lease=dict(type='int', default=86400),
                default_lease=dict(type='int', default=43200),
                enabled=dict(type='bool'),
                ip_pools=dict(
                    type='list', elements='dict',
                    options=dict(
                        start=dict(type='str'),
                        include=dict(type='str', choices=['include', 'exclude']),
                        end=dict(type='str'),
                        enabled=dict(type='bool'),
                    )
                ),
                netmask=dict(type='int'),
                default_gateway=dict(type='str'),
                dns=dict(
                    type='dict',
                    options=dict(
                        domain_name=dict(type='str'),
                        primary=dict(type='str'),
                        secondary=dict(type='str'),
                        tertiary=dict(type='str'),
                    )
                )
            )
        )
    )

    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'dhcp-server'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
