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
module: cp_gaia_physical_interface
author: Yuval Feiger (@chkp-yuvalfe)
description:
- Set Physical interface.
short_description: Set Physical interface.
version_added: '1.0.0'
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
  auto_negotiation:
    description: Activating Auto-Negotiation will skip the speed and duplex configuration.
    required: false
    type: bool
  comments:
    description: Interface Comments.
    required: false
    type: str
  duplex:
    description: Duplex for the interface. Duplex is not relevant when 'auto-negotiation' is enabled.
    required: false
    type: str
  enabled:
    description: Interface State.
    required: false
    type: bool
  ipv4_address:
    description: Interface IPv4 address.
    required: false
    type: str
  ipv4_mask_length:
    description: Interface IPv4 address mask length.
    required: false
    type: int
  ipv6_address:
    description: Interface IPv6 address.
    required: false
    type: str
  ipv6_autoconfig:
    description: Configure IPv6 auto-configuration.
    required: false
    type: bool
  ipv6_mask_length:
    description: Interface IPv6 address mask length.
    required: false
    type: int
  mac_addr:
    description: Configure hardware address.
    required: false
    type: str
  monitor_mode:
    description: Set monitor mode for the interface off/on.
    required: false
    type: bool
  mtu:
    description: Interface mtu.
    required: false
    type: int
  name:
    description: Interface name.
    required: true
    type: str
  rx_ringsize:
    description: Set receive buffer size for interface.
    required: false
    type: int
  speed:
    description: Interface link speed. Speed is not relevant when 'auto-negotiation' is enabled.
    required: false
    type: str
  tx_ringsize:
    description: Set transmit buffer size for interfaces.
    required: false
    type: int
  dhcp:
    description: DHCP configuration.
    required: false
    type: dict
    suboptions:
        enabled:
            description: Enable DHCP on this interface.
            required: False
            type: bool
        server_timeout:
            description: Specifies the amount of time, in seconds,
                         that must pass between the time that the interface begins to try to determine its address
                         and the time that it decides that it's not going to be able to contact a server.
            required: False
            type: int
            default: 60
        retry:
            description: Specifies the time, in seconds,
                         that must pass after the interface has determined that there is no DHCP server present
                         before it tries again to contact a DHCP server.
            required: False
            type: int
            default: 300
        leasetime:
            description: Specifies the lease time, in seconds, when requesting for an IP address. Default value is "default" - according to the server.
            required: False
            type: int
        reacquire_timeout:
            description: When trying to reacquire the last ip address,
                         The reacquire-timeout statement sets the time, in seconds,
                         that must elapse after the first try to reacquire the old address before it gives up and tries to discover a new address.
            required: False
            type: int
            default: 10

"""

EXAMPLES = """
- name: Set comment field of a physical interface
  check_point.gaia.cp_gaia_physical_interface:
    comments: eth0 interface
    enabled: true
    name: eth0
"""

RETURN = """
physical_interface:
  description: The updated interface details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        monitor_mode=dict(required=False, type="bool"),
        ipv6_address=dict(required=False, type="str"),
        ipv4_mask_length=dict(required=False, type="int"),
        name=dict(required=True, type="str"),
        duplex=dict(required=False, type="str"),
        tx_ringsize=dict(required=False, type="int"),
        ipv6_autoconfig=dict(required=False, type="bool"),
        enabled=dict(required=False, type="bool"),
        comments=dict(required=False, type="str"),
        mtu=dict(required=False, type="int"),
        ipv4_address=dict(required=False, type="str"),
        auto_negotiation=dict(required=False, type="bool"),
        mac_addr=dict(required=False, type="str"),
        rx_ringsize=dict(required=False, type="int"),
        speed=dict(required=False, type="str"),
        ipv6_mask_length=dict(required=False, type="int"),
        dhcp=dict(
            type='dict',
            options=dict(
                enabled=dict(type='bool'),
                server_timeout=dict(type='int', default=60),
                retry=dict(type='int', default=300),
                leasetime=dict(type='int'),
                reacquire_timeout=dict(type='int', default=10),
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'physical-interface'
    ignore = ["status"]
    show_params = ["name"]

    res = chkp_api_call(module, api_call_object, False, ignore=ignore, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
