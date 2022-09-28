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
module: cp_gaia_role
author: Ameer Asli (@chkp-ameera)
description:
- Modify role.
short_description: Modify role.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  name:
    description: Role name.
    required: true
    type: str
  features:
    description: Specifies which features will be assigned to the role.
    required: false
    type: list
    elements: dict
    suboptions:
        name:
            description: Feature name. Valid values are feature name as shown in cp_gaia_features_facts or C(all) to specify all features.
            required: False
            type: str
        permission:
            description: Feature permission. Valid values are C(read-write) C(read-only).
            required: False
            type: str
            choices: ['read-write', 'read-only']
  extended_commands:
    description:
      - Specifies which extended commands will be assigned to the role.
        Valid values are extended commands as shown in cp_gaia_extended_commands_facts API output.
    required: false
    type: list
    elements: str
"""

EXAMPLES = """
- name: Add new role
  check_point.gaia.cp_gaia_role:
    name: myrole
    extended_commands: ['LSMenabler']
    features: [{"name": "dhcp", "permission": "read-write"},
               {"name": "ntp", "permission": "read-write"},
               {"name": "syslog", "permission": "read-write"},
               {"name": "backup", "permission": "read-only"}]

"""

RETURN = """
role:
  description: The updated role details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(required=True, type='str'),
        features=dict(
            type='list', elements='dict',
            options=dict(
                name=dict(type='str'),
                permission=dict(type='str', choices=['read-write', 'read-only'])
            )
        ),
        extended_commands=dict(type='list', elements='str')
    )

    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'role'
    show_params = ['name']

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
