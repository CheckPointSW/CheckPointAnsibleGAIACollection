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
module: cp_gaia_role_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show role information.
short_description: Show role/s information.
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
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
  name:
    description: Role name to show. If not specified, all roles information is returned.
    required: false
    type: str

"""

EXAMPLES = """
- name: Show roles
  check_point.gaia.cp_gaia_role_facts:

- name: Show role by specifying it's name
  check_point.gaia.cp_gaia_role_facts:
    name: test_role

"""

RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        state:
            description: Ansible state which can be C(present) or C(absent).
            returned: always
            type: str
        name:
            description: Role name.
            returned: always
            type: str
        features:
            description: Specifies which features will be assigned to the role.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description: Feature name. Valid values are feature name as shown in cp_gaia_features_facts or C(all) to specify all features.
                    returned: always
                    type: str
                permission:
                    description: Feature permission. Valid values are C(read-write) C(read-only).
                    returned: always
                    type: str
        extended_commands:
            description:
              - Specifies which extended commands will be assigned to the role.
                Valid values are extended commands as shown in cp_gaia_extended_commands_facts API output.
            returned: always
            type: list
            elements: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        name=dict(required=False, type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'role'

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
