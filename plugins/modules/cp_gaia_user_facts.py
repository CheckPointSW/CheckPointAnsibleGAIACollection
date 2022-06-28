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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
module: cp_gaia_user_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show the users currently configured
short_description: Show user/s
version_added: '3.0.0'
options:
  name:
    description: user name to show. If not specified, all users information is returned.
    required: false
    type: str

"""

EXAMPLES = """
- name: Show users
  cp_gaia_user_facts:

- name: Show user by specifying it's name
  cp_gaia_user_facts:
    name: admin

"""

RETURN = """
ansible_facts:
  description: The user/s facts.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type="str", required=False)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "user"
    gaia_api_version = 'v1.6/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, True)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
