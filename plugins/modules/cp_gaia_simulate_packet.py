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
author: Ophir Khill (@chkp-ophirk)
description:
- simulate packet execution on both Access and NAT rulebase.
module: cp_gaia_simulate_packet
options:
    version:
        description: GAIA api version for ex 1.8
        required: False
        type: str
    ip_version:
        description: ip version of the packet.
        type: str
        required: False
        default: '4'
        choices: ['4', '6']
    source_ip:
        description: source ip of the packet.
        type: str
        required: True
    destination_ip:
        description: destination ip of the packet.
        required: True
        type: str
    ip_protocol:
        description: destination ip of the packet.
        required: True
        type: str
    protocol_options:
        description: protocol specific options.
        required: True
        type: dict
        suboptions:
            UDP:
                description: UDP specific options.
                required: False
                type: dict
                suboptions:
                    source_port:
                        description: source port of the packet.
                        required: False
                        default: '12345'
                        type: str
                    destination_port:
                        description: destination port of the packet.
                        required: True
                        type: str
            TCP:
                description: TCP specific options.
                required: False
                type: dict
                suboptions:
                    source_port:
                        description: source port of the packet.
                        required: False
                        default: '12345'
                        type: str
                    destination_port:
                        description: destination port of the packet.
                        required: True
                        type: str
            icmp:
                description: ICMP specific options.
                required: False
                type: dict
                suboptions:
                    type:
                        description: source port of the packet.
                        required: True
                        type: str
                    code:
                        description: destination port of the packet.
                        required: False
                        default: '0'
                        type: str
    incoming_interface:
        description: packet's incoming interface, set to 'localhost' for outbound packets.
        type: str
        required: True
    application:
        description: list of Applications/Categorys as defined in SmartConsole. You can specify one or more applications
        type: list
        required: False
        elements: str
    protocol:
        description: Protocol to match for services that have 'Protocol Signature' enabled.
        type: str
        required: False
    wait_for_task:
        description: Wait for task or return immediately.
        type: bool
        default: True
        required: False
short_description: installing policy
version_added: '7.0.0'
notes:
- its advisable to perform with wait_for_task set to false and refer to show_task command
"""

EXAMPLES = """
        - name: simulate packet
          check_point.gaia.cp_gaia_simulate_packet:
                    ip_version: "4"
                    source_ip: "1.2.3.4"
                    destination_ip: "2.3.4.5"
                    ip_protocol: "1"
                    protocol_options: {icmp: {type: "8"}}
                    incoming_interface: "eth0"
                    application: "Facebook"
                    protocol: "HTTP"
"""

RETURN = """
packet rulebase execution result:
  description: the NAT and Access rulebase execution result.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async


def main():
    # arguments for the module:
    fields = dict(
        ip_version=dict(type='str', choices=['4', '6'], default='4'),
        source_ip=dict(type='str', required=True),
        destination_ip=dict(type='str', required=True),
        ip_protocol=dict(type='str', required=True),
        protocol_options=dict(
            type='dict',
            required=True,
            options=dict(
                TCP=dict(
                    type='dict',
                    options=dict(
                        source_port=dict(type='str', default='12345'),
                        destination_port=dict(type='str', required=True)
                    )
                ),
                UDP=dict(
                    type='dict',
                    options=dict(
                        source_port=dict(type='str', default='12345'),
                        destination_port=dict(type='str', required=True)
                    )
                ),
                icmp=dict(
                    type='dict',
                    options=dict(
                        type=dict(type='str', required=True),
                        code=dict(type='str', default='0')
                    )
                ),
            )
        ),
        incoming_interface=dict(type='str', required=True),
        application=dict(type='list', elements='str', required=False),
        protocol=dict(type='str', required=False)
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    api_call_object = "simulate-packet"
    res = chkp_api_operation(module, api_call_object)

    # this action does not change system configuration
    res['changed'] = False

    module.exit_json(**res)


if __name__ == "__main__":
    main()
