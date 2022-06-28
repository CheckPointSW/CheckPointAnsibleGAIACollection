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
author: Ameer Asli (@chkp-ameera)
description:
- Setting message of the day
module: cp_gaia_message_of_the_day
options:
  msg:
    description: New message of the day for web, ssh and serial login.
    required: false
    type: str
  enabled:
    description: enable/disable message of the day
    required: false
    type: bool
short_description: Setting the message of the day of a machine
version_added: '3.0.0'

"""

EXAMPLES = """
- message_of_the_day: Changing the message of the day
  cp_gaia_message_of_the_day:
    msg: "Hello today"

"""

RETURN = """
message_of_the_day:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        msg=dict(type='str', required=False),
        enabled=dict(type='bool', required=False)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'message-of-the-day'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
