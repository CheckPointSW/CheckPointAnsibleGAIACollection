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
- Sets NTP status and servers.
module: cp_gaia_ntp
short_description: Sets NTP status and servers.
version_added: '3.0.0'
notes: Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    enabled:
        description: NTP active status.
        required: False
        type: bool
    servers:
        description: Servers to set. Note there cannot be more than one primary/secondary servers.
        required: False
        type: list
        elements: dict
        suboptions:
            version:
                description: NTP server version. Valid values are 1-4.
                required: False
                type: int
            type:
                description: Server type.
                required: False
                type: str
                choices: ['primary', 'secondary']
            address:
                description: Server address (IPv4/IPv6).
                required: False
                type: str
"""


EXAMPLES = """
- name: Setting ntp servers for the system
  M(cp_gaia_ntp):
    enabled: False
    servers: [{"version": 1, "type": "primary", "address": "1.1.1.1"}]
"""


RETURN = """
ntp:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type='bool'),
        servers=dict(
            type='list', elements='dict',
            options=dict(
                version=dict(type='int'),
                type=dict(type='str', choices=['primary', 'secondary']),
                address=dict(type='str')
            )
        ),
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ntp'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
