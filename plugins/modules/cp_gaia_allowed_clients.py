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
author: Ameer Asli (@chkp-ameera)
description: Modify the configuration of allowed clients.
module: cp_gaia_allowed_clients
short_description: Modify the configuration of allowed clients.
version_added: '3.0.0'
requirements: ['supported starting from gaia_api >= 1.6']
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  allowed_networks:
    description: Configure allowed clients as network.
    required: False
    type: list
    elements: dict
    suboptions:
      subnet:
        description: The network subnet.
        required: False
        type: str
      mask_length:
        description: The network mask length.
        required: False
        type: int
  allowed_hosts:
    description:
      - Configure allowed clients as hosts, valid valuse are IPv4/Ipv6 addresses.
    required: False
    type: list
    elements: str
  allowed_any_host:
    description: Allowed all hosts.
    required: False
    type: bool
  virtual_system_id:
      description: Virtual System ID.
      required: False
      type: int
notes:
- Supports C(check_mode).
'''


EXAMPLES = '''
- name: Set allowed clients
  check_point.gaia.cp_gaia_allowed_clients:
    allowed_networks: [{"subnet": "44.4.44.0", "mask_length": 24}, {"subnet": "55.4.55.0", "mask_length": 24}]
'''


RETURN = '''
allowed_clients:
  description:
    - The checkpoint object updated.
  returned: always.
  type: dict
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        allowed_networks=dict(type='list', elements='dict',
                              options=dict(
                                  subnet=dict(type='str'),
                                  mask_length=dict(type='int')
                              )
                              ),
        allowed_hosts=dict(type='list', elements='str'),
        allowed_any_host=dict(type='bool')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'allowed-clients'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
