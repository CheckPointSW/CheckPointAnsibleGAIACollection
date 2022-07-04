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
module: cp_gaia_ssh_server_settings
author: Ameer Asli (@chkp-ameera)
description:
- Modify ssh server settings.
short_description: Modify ssh server settings.
version_added: '3.0.0'
notes: Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  enabled_ciphers:
    description: Enabled ssh ciphers.
    required: False
    type: list
    elements: str
  enabled_mac_algorithms:
    description: Enabled ssh mac algorithms.
    required: False
    type: list
    elements: str
  enabled_kex_algorithms:
    description: Enabled ssh kex algorithms.
    required: False
    type: list
    elements: str
"""

EXAMPLES = """
- name: Set ssh server settings
  M(cp_gaia_ssh_server_settings):
    enabled_ciphers: ['aes128-ctr', 'aes128-gcm@openssh.com', 'aes192-ctr', 'aes256-ctr',
                      'aes256-gcm@openssh.com', 'chacha20-poly1305@openssh.com']
    enabled_kex_algorithms: ['curve25519-sha256', 'curve25519-sha256@libssh.org',
                             'diffie-hellman-group14-sha1', 'diffie-hellman-group14-sha256',
                             'diffie-hellman-group16-sha512', 'diffie-hellman-group18-sha512',
                             'diffie-hellman-group-exchange-sha256', 'ecdh-sha2-nistp256',
                             'ecdh-sha2-nistp384', 'ecdh-sha2-nistp521']
    enabled_mac_algorithms: ['hmac-sha1', 'hmac-sha1-etm@openssh.com',
                             'hmac-sha2-256', 'hmac-sha2-256-etm@openssh.com',
                             'hmac-sha2-512', 'hmac-sha2-512-etm@openssh.com',
                             'umac-64-etm@openssh.com', 'umac-64@openssh.com',
                             'umac-128-etm@openssh.com', 'umac-128@openssh.com']
"""

RETURN = """
ssh_server_settings:
  description: The updated ssh server settings details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        enabled_ciphers=dict(type='list', elements='str'),
        enabled_mac_algorithms=dict(type='list', elements='str'),
        enabled_kex_algorithms=dict(type='list', elements='str')
    )

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ssh-server-settings'
    gaia_api_version = 'v1.7/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
