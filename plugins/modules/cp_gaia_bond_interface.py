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
module: cp_gaia_bond_interface
author: Ameer Asli (@chkp-ameera)
description:
- Modify bond interface.
short_description: Modify bond interface.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
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
  name:
    description:
      - Interface name with format C(bond<id>), valid values are bond1, bond2, bond3 .. etc.
    required: true
    type: str
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
  comments:
    description: Interface Comments.
    required: false
    type: str
  enabled:
    description: Interface State.
    required: false
    type: bool
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
            description:
              - Specifies the amount of time, in seconds,
                that must pass between the time that the interface begins to try to determine its address and the time that it decides that
                it's not going to be able to contact a server.
            required: False
            type: int
            default: 60
        retry:
            description: Specifies the time, in seconds,
                         that must pass after the interface has determined that there is no DHCP server present before it tries again to contact a DHCP server.
            required: False
            type: int
            default: 300
        leasetime:
            description:
              - Specifies the lease time, in seconds,
                when requesting for an IP address. Default value is "default" - according to the server.
            required: False
            type: int
        reacquire_timeout:
            description:
              - When trying to reacquire the last ip address,
                The reacquire-timeout statement sets the time, in seconds,
                that must elapse after the first try to reacquire the old address before it gives up and tries to discover a new address
            required: False
            type: int
            default: 10
  mtu:
    description: Interface mtu.
    required: false
    type: int
  members:
    description: Interfaces members of the bond.
    required: false
    type: list
    elements: str
  xmit_hash_policy:
    description: Transmit hash policy.
    required: false
    type: str
    choices: ['layer2', 'layer3+4']
  down_delay:
    description: Down delay in milliseconds.
    required: false
    type: int
  up_delay:
    description: Up delay in milliseconds.
    required: false
    type: int
  primary:
    description: Primary member of the bond interface.
    required: false
    type: str
  lacp_rate:
    description: LACP rate.
    required: false
    type: str
    choices: ['slow', 'fast']
  mode:
    description: Primary member of the bond interface.
    required: false
    type: str
    choices: ['round-robin', 'active-backup', 'xor', '8023AD']
  mii_interval:
    description: Media monitoring interval, Valid values are C(1-5000).
    required: false
    type: int
"""

EXAMPLES = """
- name: Set comment field of a bond interface
  check_point.gaia.cp_gaia_bond_interface:
    comments: bond5 interface
    name: bond5
    mode: xor

"""

RETURN = """
bond_interface:
  description: The updated interface details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(required=True, type='str'),
        enabled=dict(type='bool'),
        comments=dict(type='str'),
        ipv4_address=dict(type='str'),
        ipv4_mask_length=dict(type='int'),
        ipv6_address=dict(type='str'),
        ipv6_autoconfig=dict(type='bool'),
        ipv6_mask_length=dict(type='int'),
        dhcp=dict(
            type='dict',
            options=dict(
                enabled=dict(type='bool'),
                server_timeout=dict(type='int', default=60),
                retry=dict(type='int', default=300),
                leasetime=dict(type='int'),
                reacquire_timeout=dict(type='int', default=10),
            )
        ),
        mtu=dict(type='int'),
        members=dict(type='list', elements='str'),
        xmit_hash_policy=dict(type='str', choices=['layer2', 'layer3+4']),
        down_delay=dict(type='int'),
        up_delay=dict(type='int'),
        primary=dict(type='str'),
        lacp_rate=dict(type='str', choices=['slow', 'fast']),
        mode=dict(type='str', choices=['round-robin', 'active-backup', 'xor', '8023AD']),
        mii_interval=dict(type='int')
    )

    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'bond-interface'
    ignore = ['status']
    show_params = ['name']
    add_params = {}
    if module.params['name'].startswith('bond') and len(module.params['name']) > 4:
        add_params = {'id': int(module.params['name'][4:])}

    res = chkp_api_call(module, api_call_object, True, ignore=ignore, show_params=show_params, add_params=add_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
