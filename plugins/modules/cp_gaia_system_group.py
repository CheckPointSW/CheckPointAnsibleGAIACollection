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
module: cp_gaia_user
author: Ameer Asli (@chkp-ameera)
description:
- Change a user's characteristics.
short_description: Change a user's characteristics.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
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
    description: User name.
    required: True
    type: str
  shell:
    description: Specifies the user's default command line interpreter during login.
    required: False
    default: 'cli'
    type: str
    choices: ['scp-only', 'tcsh', 'csh', 'sh', 'no-login', 'bash' ,'cli']
  homedir:
    description:
      - Specifies the user's home directory as the full UNIX path name where the user is placed on login.
        If the directory doesn't exist, it is created.
        Range  Must be under '/home' and must not contain colon.
        Unless set, the default 'homedir' will be '/home/user-name'.
    required: False
    type: str
  secondary_system_groups:
    description: This operation sets the groups of the user. Valid values must be names of known groups.
    required: False
    type: list
    elements: str
  password_hash:
    description: An encrypted representation of the password. Hash version of a password can be generated using the 'grub-md5-crypt' utility.
    required: False
    type: str
  must_change_password:
    description:
      - Forcing password change is relevant only when a password is set.
        When set to 'True' Force the user to change their password the next time they log in.
        If they don't log in within the time limit configured in 'set password-controls expiration-lockout-days' they may not be able to log in at all.
        When set to 'False' If the user was being forced to change their password, cancel that.
        If the user was locked out due to failure to change their password
        within the time limit configured in 'set password-controls expiration-lockout-days'
        they will no longer be locked out.
    required: False
    type: bool
  real_name:
    description: Specifies a string describing a user; conventionally it's the user's full name. Default is Username, capitalized.
    required: False
    type: str
  unlock:
    description: If the user has been locked out, cancel that. True cancel lock-out. False  do nothing.
    required: False
    type: bool
  allow_access_using:
    description: Modify the access-mechanisms available for a user. Valid values are C(CLI) C(Web-UI) C(Gaia-API) (supported from R81.10).
    required: False
    type: list
    elements: str
    choices: ['CLI', 'Web-UI', 'Gaia-API']
    default: ['CLI', 'Web-UI']
  roles:
    description: Roles spesified to the user.
    required: False
    type: list
    elements: str
  primary_system_group_id:
    description: GID. Numeric ID which is used in identifying the primary group to which this user belongs.
    required: False
    type: int
    default: 100
  password:
    description: Specifies new password on command line.
                 Check Point recommends that a password be at least eight characters long.
                 A password must contain at least six characters.
                 Enforcement level can be modified via 'password control' feature.
    required: False
    type: str
  uid:
    description: Specifies a numeric user ID used to identify permissions of a user, duplicate UIDs are not allowed.
    required: False
    type: int
"""

EXAMPLES = """
- name: Set shell field for the user
  check_point.gaia.cp_gaia_user:
    shell: bash
    name: admin

"""

RETURN = """
user:
  description: The updated user details.
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
    ignore = []
    show_params = ["name"]

    res = chkp_api_call(module, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
