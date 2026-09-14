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
                description: Server type. C(server) and C(pool) require Gaia API v1.8 or above.
                             C(primary) and C(secondary) are supported on all versions.
                required: False
                type: str
                choices: ['primary', 'secondary', 'server', 'pool']
            address:
                description: Server address (IPv4/IPv6).
                required: False
                type: str
    preferred:
        description: Preferred address. Specify a particular server as preferred above others of
                     similar statistical quality. Requires Gaia API v1.8 or above.
        required: False
        type: str
"""


EXAMPLES = """
- name: Setting ntp servers for the system
  check_point.gaia.cp_gaia_ntp:
    enabled: false
    servers: [{"version": 1, "type": "primary", "address": "1.1.1.1"}]
"""


RETURN = """
ntp:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


API_VERSION_SERVER_POOL_TYPES = (1, 8)


def _parse_api_version(version):
    if version is None:
        return None
    try:
        return tuple(int(part) for part in str(version).split('.'))
    except ValueError:
        return None


def _fail_if_unsupported(module, api_version):
    if api_version is None or api_version >= API_VERSION_SERVER_POOL_TYPES:
        return
    minimum = 'v{0}.{1}'.format(*API_VERSION_SERVER_POOL_TYPES)
    requested = module.params.get('version')
    if module.params.get('preferred') is not None:
        module.fail_json(msg="'preferred' requires Gaia API {0} or above, but version {1} was requested".format(
            minimum, requested))
    for server in module.params.get('servers') or []:
        if server and server.get('type') in ('server', 'pool'):
            module.fail_json(msg="Server type '{0}' requires Gaia API {1} or above, but version {2} was requested".format(
                server['type'], minimum, requested))


def _normalize_server_for_compare(server, api_version):
    normalized = {}
    if server.get('address') is not None:
        normalized['address'] = server['address']
    version = server.get('version') if server.get('version') is not None else server.get('ver')
    if version is not None:
        normalized['ver'] = str(version)
    server_type = server.get('type')
    if server_type is not None:
        if api_version is not None and api_version < API_VERSION_SERVER_POOL_TYPES:
            normalized['type'] = server_type
        elif server_type in ('primary', 'secondary'):
            normalized['type'] = 'server'
        else:
            normalized['type'] = server_type
    return normalized


def main():
    fields = dict(
        enabled=dict(type='bool'),
        servers=dict(
            type='list', elements='dict',
            options=dict(
                version=dict(type='int'),
                type=dict(type='str', choices=['primary', 'secondary', 'server', 'pool']),
                address=dict(type='str')
            )
        ),
        preferred=dict(type='str'),
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ntp'
    api_version = _parse_api_version(module.params.get('version'))

    _fail_if_unsupported(module, api_version)

    compare_params = {}
    if module.params.get('enabled') is not None:
        compare_params['enabled'] = module.params['enabled']
    if module.params.get('servers') is not None:
        compare_params['servers'] = [
            _normalize_server_for_compare(s, api_version)
            for s in module.params['servers']
            if s is not None
        ]
    if module.params.get('preferred') is not None:
        compare_params['preferred'] = module.params['preferred']

    res = chkp_api_call(module, api_call_object, False, ignore=['status'], compare_params=compare_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
