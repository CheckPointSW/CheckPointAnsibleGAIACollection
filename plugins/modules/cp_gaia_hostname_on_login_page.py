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
- Setting the hostname on login page message.
module: cp_gaia_hostname_on_login_page
options:
  enabled:
    description: Hostname on WebUI login page enabled.
    required: false
    type: bool
    default: False
short_description: Enable/disable the hostname on login page message.
version_added: '3.0.0'
notes:
- Supports C(check_mode).

"""

EXAMPLES = """
- hostname_on_login_page: Changing the banner message
  check_point.gaia.cp_gaia_hostname_on_login_page:
    enabled: True

"""

RETURN = """
hostname_on_login_page:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type='bool', required=False, default=False)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'hostname-on-login-page'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
