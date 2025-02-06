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
module: cp_gaia_virtual_gateway
short_description: Manages virtual gateway on Check Point Gateway over Web Services API
description:
  - Manages virtual gateway on Check Point gateways including creating, updating, and removing virtual systems.
  - All operations are performed over Web Services API.
version_added: "6.0.0"
author: Omer Hadad (@chkp-omerhad)
options:
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    choices: ['present', 'absent']
    default: present
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  wait_for_task:
    description: Wait for task or return immediately.
    required: False
    default: True
    type: bool
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
  id:
    description:
      - Virtual gateway ID.
      - This parameter is used to change an existing virtual gateway or create a new one if it does not exist.
    type: str
  name:
    description:
      - Name of the virtual gateway.
      - This parameter is used to change an existing virtual gateway by name.
    type: str
  one_time_password:
    description:
      - One-time password of the virtual gateway.
      - This parameter is used to set the one-time password for an existing virtual gateway by name or ID.
    type: str
  interfaces:
    description:
      - Configure interfaces for the virtual gateway.
      - Collection of interfaces to be set, identified by the name. Replaces existing interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Interface name.
        type: str
  resources:
      description:
        - Virtual gateway resources configuration.
      type: dict
      suboptions:
        firewall_ipv4_instances:
          description:
            - The number of IPv4 CoreXL instances to be assigned to the virtual gateway identified by name or ID.
          type: int
        firewall_ipv6_instances:
          description:
            - The number of IPv6 CoreXL instances to be assigned to the virtual gateway identified by name or ID.
          type: int
  virtual_switches:
      description:
        - Connect virtual gateway identified by name or ID to pre-existing virtual switches identified by their IDs.
        - Collection of virtual switches to be set, identified by their IDs. Replaces existing interfaces.
      type: list
      elements: dict
      suboptions:
        id:
          description: Virtual switch ID.
          type: int
  mgmt_connection:
    description:
      - Management connection configuration.
    type: dict
    suboptions:
      mgmt_connection_identifier:
        description:
          - Management connection identifier.
          - This parameter is used to change an existing virtual gateway by name.
        type: str
        required: true
      mgmt_connection_type:
        description:
          - Management connection type.
          - This parameter is used to change an existing virtual gateway by name.
        type: str
        required: true
        choices: ['interface', 'virtual-switch-id', 'virtual-switch-name']
      mgmt_ipv4_configuration:
        description:
          - Management connection IPv4 configuration.
        type: dict
        suboptions:
          ipv4_address:
            description:
              - Management connection IPv4 address.
            type: str
            required: true
          ipv4_mask:
            description:
              - Management connection IPv4 mask length.
            type: int
            required: true
          ipv4_default_gateway:
            description:
              - Management connection IPv4 default gateway.
            type: str
      mgmt_ipv6_configuration:
        description:
          - Management connection IPv6 configuration.
        type: dict
        suboptions:
          ipv6_address:
            description:
              - Management connection IPv6 address.
            type: str
            required: true
          ipv6_mask:
            description:
              - Management connection IPv6 mask length.
            type: int
            required: true
          ipv6_default_gateway:
            description:
              - Management connection IPv6 default gateway.
            type: str
"""
EXAMPLES = """
- name: set virtual gateway
  check_point.gaia.cp_gaia_virtual_gateway:
    id: 11
    one_time_password: dummyOTP
    interfaces:
      - name: eth1-02.2
      - name: eth1-02.3
    virtual_switches:
      - id: 1
      - id: 500
    resources:
      firewall_ipv4_instances: 2
      firewall_ipv6_instances: 0
    mgmt_connection:
      mgmt_connection_identifier: 500
      mgmt_connection_type: virtual-switch-id
      mgmt_ipv4_configuration:
        ipv4_address: 172.72.72.1
        ipv4_mask: 24
        ipv4_default_gateway: 172.72.72.4
"""
RETURN = """
cp_gaia_virtual_system:
  description: virtual gateway creation output.
  returned: always.
  type: dict
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import (
    chkp_api_call,
    checkpoint_argument_spec_for_all,
    checkpoint_argument_spec_for_async,
)


def run_module():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        id=dict(type='str'),
        name=dict(type='str'),
        one_time_password=dict(type='str', no_log=True),
        interfaces=dict(type='list', elements='dict', options=dict(name=dict(type='str'))),
        virtual_switches=dict(type='list', elements='dict', options=dict(id=dict(type='int'))),
        resources=dict(
            type='dict',
            options=dict(
                firewall_ipv4_instances=dict(type='int'),
                firewall_ipv6_instances=dict(type='int')
            )
        ),
        mgmt_connection=dict(
            type='dict',
            options=dict(
                mgmt_connection_identifier=dict(type='str', required=True),
                mgmt_connection_type=dict(type='str', required=True, choices=['interface', 'virtual-switch-id', 'virtual-switch-name']),
                mgmt_ipv4_configuration=dict(
                    type='dict',
                    required=False,
                    options=dict(
                        ipv4_address=dict(type='str', required=True),
                        ipv4_mask=dict(type='int', required=True),
                        ipv4_default_gateway=dict(type='str', required=False)
                    )
                ),
                mgmt_ipv6_configuration=dict(
                    type='dict',
                    required=False,
                    options=dict(
                        ipv6_address=dict(type='str', required=True),
                        ipv6_mask=dict(type='int', required=True),
                        ipv6_default_gateway=dict(type='str', required=False)
                    )
                )
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    ignore = ['status']
    show_params = ['id']
    add_params = {'id': module.params['id']}
    api_call_object = "virtual-gateway"
    res = chkp_api_call(module, api_call_object, True, ignore=ignore, show_params=show_params, add_params=add_params)
    module.exit_json(**res)


def main():
    run_module()


if __name__ == '__main__':
    main()
