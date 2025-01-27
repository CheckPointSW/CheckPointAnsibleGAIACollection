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
  - Modify the configuration of static route.
module: cp_gaia_static_route
short_description: Modify the configuration of static route.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    version:
      description: Gaia API version for example 1.6.
      required: False
      type: str
    virtual_system_id:
      description: Virtual System ID.
      required: False
      type: int
    address:
        description: IPv4 address.
        required: True
        type: str
    mask_length:
        description: Mask length address.Valid values are 0-32.
        required: True
        type: int
    type:
        description: Type of next hop.
        required: True
        type: str
        choices: ['blackhole', 'gateway', 'reject']
    state:
        description: Ansible state which can be C(present) or C(absent).
        required: False
        type: str
        default: present
        choices: [present, absent]
    next_hop:
        description:
          - Static next_hop. Contains a list of next-hop gateways.
        required: False
        type: list
        elements: dict
        suboptions:
            gateway:
                description: IP address or logical name for the static next-hop gateway.
                required: False
                type: str
            priority:
                description:
                  - Priority defines which gateway to select as the next-hop.
                  - The lower the priority, the higher the preference.
                  - Possible values are 1-8.
                required: False
                type: int
    comment:
        description: Static route comment.
        required: False
        type: str
    rank:
        description:
          - Selects a route when there are many routes to a destination that use different routing protocols.
          - The route with the lowest rank value is selected. Possible values are 0-255.
        required: False
        type: int
    ping:
        description: Configures ping monitoring of the given IPv4 static route.
        required: False
        type: bool
        default: False
    scope_local:
        description: Configure the local interface scope option, When the this option is enabled, the route treated as directly connected to local machine.
        required: False
        type: bool
        default: False
"""


EXAMPLES = """
- name: Set new static route
  check_point.gaia.cp_gaia_static_route:
    state: present
    address: 1.2.125.0
    mask_length: 24
    type: gateway
    next_hop: [{"gateway": "1.1.1.1", "priority": 2}]

"""


RETURN = """
static_route:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type="str", default="present", choices=['present', 'absent']),
        address=dict(type="str", required=True),
        mask_length=dict(type="int", required=True),
        type=dict(type="str", required=True, choices=['blackhole', 'gateway', 'reject']),
        next_hop=dict(
            type='list', elements='dict',
            options=dict(
                priority=dict(type='int'),
                gateway=dict(type='str')
            )
        ),
        comment=dict(type='str'),
        rank=dict(type='int'),
        ping=dict(type='bool', default=False),
        scope_local=dict(type='bool', default=False),
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(
        argument_spec=fields,
        required_if=[
            ('state', 'present', ('type',)),
            ('type', 'gateway', ('next_hop',))
        ],
        supports_check_mode=True
    )

    api_call_object = 'static-route'
    show_params = ["address", "mask_length"]

    res = chkp_api_call(module, api_call_object, False, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
