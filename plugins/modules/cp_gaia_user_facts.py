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
module: cp_gaia_user_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show the users currently configured.
short_description: Show user/s.
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
  name:
    description: User name to show. If not specified, all users information is returned.
    required: false
    type: str

"""

EXAMPLES = """
- name: Show users
  check_point.gaia.cp_gaia_user_facts:

- name: Show user by specifying it's name
  check_point.gaia.cp_gaia_user_facts:
    name: admin

"""

RETURN = """
ansible_facts:
    description: The user/s facts.
    returned: always.
    type: dict
    contains:
        objects:
            description:
              - List of users.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description:
                      - User name.
                    returned: always
                    type: str
                uid:
                    description:
                      - User UID.
                    returned: always
                    type: int
                homedir:
                    description:
                      - User home directory.
                    returned: always
                    type: str
                primary_system_group_id:
                    description:
                      - User primary system group id.
                    returned: always
                    type: int
                secondary_system_groups:
                    description:
                      - User secondary system groups.
                    returned: always
                    type: list
                    elements: str
                real_name:
                    description:
                      - User real name.
                    returned: always
                    type: str
                shell:
                    description:
                      - User shell.
                    returned: always
                    type: str
                allow_access_using:
                    description:
                      - The access-mechanisms available for a user. Valid values CLI, Web-UI, Gaia-API (supported from R81.10). Default [CLI, Web-UI].
                    returned: always
                    type: list
                    elements: str
                must_change_password:
                    description:
                      - Must_change_password.
                    returned: always
                    type: bool
                roles:
                    description:
                      - User roles.
                    returned: always
                    type: list
                    elements: str
                locked:
                    description:
                      - If the user has been locked out.
                    returned: always
                    type: bool
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type="str", required=False)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "user"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
