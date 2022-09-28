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
- Run First Time Wizard configuration.
module: cp_gaia_initial_setup
options:
  wait_for_task:
    description: Wait for task or return immediately.
    required: False
    default: True
    type: bool
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  password:
    description: Password of user admin. Required in case default initial password has not been changed before.
    required: False
    type: str
  security_management:
    description: Install Security Management or Multi domain server.
    required: False
    type: dict
    suboptions:
      multi_domain:
        description: Install Security Multi domain server, it can be C(primary) or C(secondary) or C(log-server) according to type parameter.
        required: False
        default: False
        type: bool
      type:
        description: Type of security management or multi domain server.
        required: False
        choices: [primary, secondary, log-server]
        default: primary
        type: str
      activation_key:
        description: Secure Internal Communication key, relevant in case of secondary or log-server.
        required: False
        type: str
      leading_interface:
        description: Leading multi domain server interface, relevant in case of multi-domain enabled.
        required: False
        type: str
      gui_clients:
        description:
          - Choose which GUI clients can log into the Security Management.
            fill one of the parameters C(range) C(network) C(single-ip),
            for multi-domain it can be only single-ip or can keep the default value.
        required: False
        type: dict
        suboptions:
            range:
              description: Range of IPs allowed to connect to management.
              required: False
              type: dict
              suboptions:
                  first_IPv4_range:
                    description: First IP in range.
                    required: False
                    type: str
                  last_IPv4_range:
                    description: Last IP in range.
                    required: False
                    type: str
            network:
              description: IPs from specific network allowed to connect to management.
              required: False
              type: dict
              suboptions:
                  address:
                    description: IPv4 address of network.
                    required: False
                    type: str
                  mask_length:
                    description: Mask length of network.
                    required: False
                    type: int
            single_ip:
              description: In case of a single IP which allowed to connect to management.
              required: False
              type: str
  security_gateway:
    description: Install Security Gateway.
    required: False
    type: dict
    suboptions:
      dynamically_assigned_ip:
        description:
          - Enable DAIP (dynamic ip) gateway. Should be false if cluster_member or security_management enabled.
        required: False
        default: False
        type: bool
      cluster_member:
        description: Enable/Disable ClusterXL.
        required: False
        default: False
        type: bool
      activation_key:
        description: Secure Internal Communication key.
        required: False
        type: str
short_description: Run First Time Wizard configuration.
version_added: '3.0.0'
notes:
- Supports C(check_mode).

"""


EXAMPLES = """
- name: Initial setup
  check_point.gaia.cp_gaia_initial_setup:
    wait_for_task: True
    security_gateway: {cluster_member: False, activation_key: bbbb, dynamically_assigned_ip: False}
"""

RETURN = """
initial_setup:
  description: The checkpoint object updated.
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
        password=dict(type="str", required=False, no_log=True),
        security_management=dict(
            type='dict',
            options=dict(
                multi_domain=dict(type='bool', required=False, default=False),
                type=dict(type='str', choices=['primary', 'secondary', 'log-server'], default='primary'),
                activation_key=dict(type='str', required=False, no_log=True),
                leading_interface=dict(type='str', required=False),
                gui_clients=dict(
                    type='dict',
                    options=dict(
                        range=dict(
                            type='dict',
                            options=dict(
                                first_IPv4_range=dict(type='str'),
                                last_IPv4_range=dict(type='str')
                            )
                        ),
                        network=dict(
                            type='dict',
                            options=dict(
                                address=dict(type='str'),
                                mask_length=dict(type='int')
                            )
                        ),
                        single_ip=dict(type='str')
                    )
                )
            )
        ),
        security_gateway=dict(
            type='dict',
            options=dict(
                dynamically_assigned_ip=dict(type='bool', required=False, default=False),
                cluster_member=dict(type='bool', required=False, default=False),
                activation_key=dict(type='str', required=False, no_log=True)
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-initial-setup'

    # Run the command:
    res = chkp_api_operation(module, api_call_object)

    module.exit_json(**res)


if __name__ == "__main__":
    main()
