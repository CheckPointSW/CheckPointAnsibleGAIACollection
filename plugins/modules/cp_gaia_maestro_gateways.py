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

DOCUMENTATION = '''
---
author: Roi Tal (@chkp-roital)
description: Assign, re-assign or un-assign Gateways to Security Groups, and change GW descriptions.
module: cp_gaia_maestro_gateways
short_description: Modify Security Group Members.
version_added: '3.0.0'
requirements: ['supported starting from gaia_api >= 1.8']
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  id:
    description: The serial of the Gateway you wish to modify
    required: True
    type: str
  security_group:
    description: Choose ID of Security Group to assign this Gateway to
    required: False
    type: int
  description:
    description: Description of this Gateway
    required: False
    type: str

notes:
- Supports C(check_mode).
'''

EXAMPLES = """
- name: Assign GW to SG and add description
  check_point.gaia.cp_gaia_gateways:
    id: 1007RT1992
    security_group: 1
    description: "1007RT1992 GW Description"

"""

RETURN = """
maestro_gateway:
  description: The updated Maestro Gateway details.
  returned: always.
  type: dict  
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all

def main():
    # arguments for the module:
    fields = dict(
        id=dict(type='str', required=True),
        security_group=dict(type="int"),
        description=dict(type="str")
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'maestro-gateway'
    show_params = ["id"]
    res = chkp_api_call(module, api_call_object, False, show_params=show_params)
    module.exit_json(**res)

if __name__ == "__main__":
    main()
