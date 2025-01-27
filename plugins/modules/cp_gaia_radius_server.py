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
- Set radius servers settings.
module: cp_gaia_radius_server
short_description: Set radius servers settings.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
  super_user_uid:
        description: The UID that will be given to a super user.
        required: False
        type: str
        choices: ['0', '96']
  default_shell:
        description: Default shell when login.
        required: False
        type: str
        choices: ['scp-only', 'tcsh', 'csh', 'sh', 'no-login', 'bash', 'cli']
  nas_ip:
        description: The NAS IP for the radius client.
        required: False
        type: str
  servers:
        description: Radius servers list.
        required: False
        type: list
        elements: dict
        suboptions:
            priority:
                description: Search priority (lower values comes first). Valid values are -999 - 999.
                required: False
                type: int
            secret:
                description: Secret string.
                required: False
                type: str
            port:
                description: UDP port to contact on the RADIUS server.
                required: False
                type: int
            timeout:
                description: Valid values are 1-50.
                required: False
                type: int
            address:
                description: Server address.
                required: False
                type: str
"""


EXAMPLES = """
- name: Change Radius server settings
  check_point.gaia.cp_gaia_radius_server:
    default_shell: cli
    servers: [{"priority": 3, "address": "1.2.1.2", "port": 56, "timeout": 1, "secret": "12345"}]
"""


RETURN = """
radius:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        super_user_uid=dict(type='str', choices=['0', '96']),
        default_shell=dict(type='str', choices=['scp-only', 'tcsh', 'csh', 'sh', 'no-login', 'bash', 'cli']),
        nas_ip=dict(type='str'),
        servers=dict(
            type='list', elements='dict',
            options=dict(
                priority=dict(type='int'),
                secret=dict(type='str', no_log=True),
                port=dict(type='int'),
                timeout=dict(type='int'),
                address=dict(type='str')
            )
        )
    )

    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'radius'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
