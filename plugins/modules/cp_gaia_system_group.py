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
module: cp_gaia_system_group
author: Duane Toler (@duanetoler)
description:
- Change system group configuration.
short_description: Change system group configuration.
version_added: '8.0.0'
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
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  name:
    description: System group name.
    required: True
    type: str
  gid:
    description: Specifies a numeric group ID used to identify the group, duplicate GIDs are not allowed.
    required: False
    type: int
  users:
    description: List of users in the group.
    required: False
    type: list
    elements: str
"""

EXAMPLES = """
- name: Add new system group
  check_point.gaia.cp_gaia_system_group:
    name: new_group
    members:
      - admin
"""

RETURN = """
group:
  description: The updated group details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(type='str', required=True),
        gid=dict(type='int', required=False),
        users=dict(type='list', elements='str', required=False)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'system-group'
    show_params = ["name"]

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
