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
- Change proxy setting.
module: cp_gaia_proxy
short_description: Change proxy setting.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
options:
    state:
        description: Ansible state which can be C(present) or C(absent).
        required: False
        type: str
        default: present
        choices: [present, absent]
    address:
        description: IPv4/IPv6 address.
        required: False
        type: str
    port:
        description: Proxy server port.
        required: False
        type: int
"""


EXAMPLES = """
- name: Set new static route
  check_point.gaia.cp_gaia_proxy:
    state: present
    address: 1.2.125.0
    port: 89

"""


RETURN = """
proxy:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        address=dict(type='str'),
        port=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=fields,
        required_if=[
            ('state', 'present', ('address', 'port', ))
        ],
        supports_check_mode=True
    )
    api_call_object = 'proxy'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
