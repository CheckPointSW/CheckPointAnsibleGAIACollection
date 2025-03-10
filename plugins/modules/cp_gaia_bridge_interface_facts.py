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
module: cp_gaia_bridge_interface_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show bridge interface.
short_description: Show bridge interface/s.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  name:
    description: Interface name to show. If not specified, all bridge interfaces information is returned.
    required: false
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: false
    type: int
"""

EXAMPLES = """
- name: Show bridge interface
  check_point.gaia.cp_gaia_bridge_interface_facts:

- name: Show bridge interface by specifying it's name
  check_point.gaia.cp_gaia_bridge_interface_facts:
    name: br1
"""

RETURN = """
ansible_facts:
    description: The interface/s facts.
    returned: always.
    type: dict
    contains:
        objects:
            description:
              - List of interfaces.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description:
                      - Interface name.
                    returned: always
                    type: str
                virtual_system_id:
                    description: Virtual System ID.
                    returned: always
                    type: int
                ipv4_address:
                    description: Interface IPv4 address.
                    returned: always
                    type: str
                ipv4_mask_length:
                    description: Interface IPv4 address mask length.
                    returned: always
                    type: int
                ipv6_address:
                    description: Interface IPv6 address.
                    returned: always
                    type: str
                ipv6_autoconfig:
                    description: Configure IPv6 auto-configuration.
                    returned: always
                    type: bool
                ipv6_mask_length:
                    description: Interface IPv6 address mask length.
                    returned: always
                    type: int
                comments:
                    description: Interface Comments.
                    returned: always
                    type: str
                enabled:
                    description: Interface State.
                    returned: always
                    type: bool
                dhcp:
                    description: DHCP configuration.
                    returned: always
                    type: dict
                    contains:
                        enabled:
                            description: Enable DHCP on this interface.
                            returned: always
                            type: bool
                        server_timeout:
                            description: Specifies the amount of time, in seconds,
                                         that must pass between the time that the interface begins to try to determine its address
                                         and the time that it decides that it's not going to be able to contact a server.
                            returned: always
                            type: int
                        retry:
                            description: Specifies the time, in seconds,
                                         that must pass after the interface has determined that there is no DHCP server present
                                         before it tries again to contact a DHCP server.
                            returned: always
                            type: int
                        leasetime:
                            description:
                              - Specifies the lease time, in seconds, when requesting for an IP address.
                                Default value is "default" - according to the server.
                            returned: always
                            type: int
                        reacquire_timeout:
                            description:
                              - When trying to reacquire the last ip address,
                                The reacquire-timeout statement sets the time, in seconds,
                                that must elapse after the first try to reacquire the old address before it gives up and
                                tries to discover a new address.
                            returned: always
                            type: int
                mtu:
                    description: Interface mtu.
                    returned: always
                    type: int
                ipv6_local_link_address:
                    description: Interface ipv6 local link address.
                    returned: always
                    type: str
                status:
                    description: Interface data.
                    returned: always
                    type: dict
                    contains:
                        link_state:
                            description: Link status.
                            returned: always
                            type: bool
                        speed:
                            description: Speed.
                            returned: always
                            type: str
                        duplex:
                            description: Duplex.
                            returned: always
                            type: str
                        tx_bytes:
                            description: TX bytes.
                            returned: always
                            type: int
                        tx_packets:
                            description: TX packets.
                            returned: always
                            type: int
                        rx_bytes:
                            description: RX bytes.
                            returned: always
                            type: int
                        rx_packets:
                            description: RX packets.
                            returned: always
                            type: int
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        name=dict(required=False, type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "bridge-interface"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
