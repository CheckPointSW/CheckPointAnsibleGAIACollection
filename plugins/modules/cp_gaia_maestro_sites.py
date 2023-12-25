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
description: Set site description.
module: cp_gaia_maestro_sites
short_description: Set site description.
version_added: '3.0.0'
requirements: ['supported starting from gaia_api >= 1.8']
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  site-id:
    description: ID of site.
    required: True
    type: int
  descriptions:
    description: Provide optional site description per Security Group.
    required: False
    type: list
    elements: dict
    contains:
      security-group:
        description: The Site Security Group
        type: int
      description:
        description: Site description
        type: str
        
notes:
- Supports C(check_mode).
'''

EXAMPLES = """
- name: Set site 1 description
  check_point.gaia.cp_gaia_sites:
    site_id: 1
    descriptions: {security_group: 1, description: "New Description"}

"""

RETURN = """
maestro_site:
  description: The updated site details.
  returned: always.
  type: dict  
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all

def main():
    # arguments for the module:
    fields = dict(
        site_id=dict(type='int', required=True),
        descriptions=dict(
            type="list", elements="dict",
            options=dict(
                security_group=dict(type="int"),
                description=dict(type="str")
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'maestro-site'
    show_params = ["site_id"]
    res = chkp_api_call(module, api_call_object, False, show_params=show_params)
    module.exit_json(**res)

if __name__ == "__main__":
    main()
