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
author: Yuval Feiger (@chkp-yuvalfe)
description:
- Setting the hostname of a machine.
module: cp_gaia_hostname
options:
  name:
    description: New hostname to change. Hostname can be a combination of letters and numbers, it cannot
      be in IP format or start/end with characters such as ''.'' And ''-''.
    required: true
    type: str
short_description: Setting the hostname of a machine.
version_added: '1.0.0'
notes: Supports C(check_mode).

"""

EXAMPLES = """
- name: Changing a hostname
  M(cp_gaia_hostname):
    name: new-hostname

"""

RETURN = """
hostname:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type='str', required=True)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'hostname'
    gaia_api_version = 'v1.6/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
