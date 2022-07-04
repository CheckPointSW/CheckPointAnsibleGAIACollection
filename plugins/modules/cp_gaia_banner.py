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
- Setting the banner message.
module: cp_gaia_banner
options:
  msg:
    description: Banner message for the web, ssh and serial login. Empty string returns to default.
    required: false
    type: str
    default: "This system is for authorized use only."
  enabled:
    description: Banner message enabled.
    required: false
    type: bool
short_description: Setting the banner message.
version_added: '3.0.0'
notes: Supports C(check_mode).

"""

EXAMPLES = """
- banner: Changing the banner message
  M(cp_gaia_banner):
    msg: new_message

"""

RETURN = """
banner:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        msg=dict(type='str', required=False, default="This system is for authorized use only."),
        enabled=dict(type='bool', required=False)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'banner'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
