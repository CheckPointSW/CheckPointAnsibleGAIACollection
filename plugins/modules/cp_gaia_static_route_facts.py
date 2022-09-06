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
- Show the configuration of static route.
module: cp_gaia_static_route_facts
short_description: Show the configuration of static route.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    limit:
        description: The maximum number of returned results. relevant in case facts for all routes.
        required: False
        default: 50
        type: int
    offset:
        description: The number of results to initially skip. relevant in case facts for all routes.
        required: False
        default: 0
        type: int
    order:
        description:
          - Sorts the routes by either ascending or descending order. Valid values are C(ASC) C(DESC). relevant in case facts for all routes.
        required: False
        type: str
        default: ASC
        choices: ['ASC', 'DESC']
    address:
        description: Existing IPv4 address, required in case fact for single route.
        required: False
        type: str
    mask_length:
        description: Existing mask length address.Valid values are 0-32, required in case fact for single route.
        required: False
        type: int
"""


EXAMPLES = """
- name: Show active static routes
  check_point.gaia.cp_gaia_static_route_facts:
"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        total:
            description: Total number of routes.
            returned: always
            type: int
        from:
            description: From which route the query was done.
            returned: always
            type: int
        to:
            description: To which route the query was done.
            returned: always
            type: int
        objects:
            description: List of all aggregate routes.
            returned: always
            type: list
            elements: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict(
        address=dict(type="str"),
        mask_length=dict(type="int"),
        limit=dict(type="int", required=False, default=50),
        offset=dict(type="int", required=False, default=0),
        order=dict(type="str", required=False, default='ASC', choices=['ASC', 'DESC'])
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True, required_together=[('address', 'mask_length')])

    api_call_object = 'static-route'
    gaia_api_version = 'v1.6/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
