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

DOCUMENTATION = '''
---
author: Roi Tal (@chkp-roital)
description: Set Port configuration. Note that at least one of 'id' or 'interface-name' must be provided.
module: cp_gaia_maestro_gateways
short_description: Set Port configuration.
version_added: '7.0.0'
requirements: ['supported starting from gaia_api >= 1.8']
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  id:
    description: Port ID (e.g. '1/13/1').
    required: False
    type: str
  interface_name:
    description: Interface name in case this port is an Uplink or MGMT interface (e.g. 'eth1-25').
    required: False
    type: str
  enabled:
    description: Setting this to false will disable this port, setting to true will enable it. AKA 'admin state'.
    required: False
    type: bool
  mtu:
    description: MTU of this port.
    required: False
    type: int
  auto_negotiation:
    description: If true, Auto Negotiation will be turned on, and vice versa.
    required: False
    type: bool
  qsfp_mode:
    description: Port QSFP mode. 
    required: False
    choices: ['4x10G', '4x25G', '25G', '40G', '100G']
    type: str
  type:
    description: Port type.
    reuired: False
    choices: ['downlink', 'uplink', 'site_sync', 'ssm_sync', 'mgmt']
    type: str

notes:
- Supports C(check_mode).
'''

EXAMPLES = """
- name: Change port QSFP mode
  check_point.gaia.cp_gaia_ports:
    id: 1/1/1
    qsfp_mode : 4x25G
"""

RETURN = """
maestro_port:
  description: The updated Port details.
  returned: always.
  type: dict  
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all

def main():
    # arguments for the module:
    fields = dict(
        id=dict(type='str'),
        interface_name=dict(type='str'),
        enabled=dict(type='bool'),
        mtu=dict(type='int'),
        auto_negotiation=dict(type='bool'),
        qsfp_mode=dict(type='str', choices=['4x10G', '4x25G', '25G', '40G', '100G']),
        type=dict(type='str', choices=['downlink', 'uplink', 'site_sync', 'ssm_sync', 'mgmt'])
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'maestro-port'
    show_params = ["id", "interface_name"]
    res = chkp_api_call(module, api_call_object, False, show_params=show_params)
    module.exit_json(**res)

if __name__ == "__main__":
    main()
