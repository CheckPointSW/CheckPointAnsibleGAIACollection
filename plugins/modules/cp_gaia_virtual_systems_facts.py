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
description:
- Show Virtual Systems.
module: cp_gaia_virtual_systems_facts
options:
  version:
    description: Gaia API version for example 1.8.
    required: False
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
short_description: Show Virtual Systems.
version_added: '6.0.0'
author: Omer Hadad (@chkp-omerhad)
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.8
"""

EXAMPLES = """
- name: Show Virtual Systems
  check_point.gaia.cp_gaia_virtual_systems_facts:
"""

RETURN = """
ansible_facts:
    description: The Virtual Systems facts.
    returned: always.
    type: dict
    contains:
        objects:
            description: List of configured Virtual Systems.
            returned: always
            type: list
            elements: dict
            contains:
                id:
                    description: Virtual System ID.
                    returned: always
                    type: int
                name:
                    description: Virtual System name.
                    returned: always
                    type: str
                virtual_system_type:
                    description: Virtual System type, Gateway or Switch.
                    returned: always
                    type: str
                interfaces:
                    description: Network interfaces attached to the Virtual System.
                    returned: always
                    type: list
                    elements: str
        from:
            description: From which element number the query was done.
            returned: always
            type: int
        to:
            description: To which element number the query was done.
            returned: always
            type: int
        total:
            description: Total number of elements returned by the query.
            returned: always
            type: int
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def run_module():
    fields = dict()
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'virtual-systems'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


def main():
    run_module()


if __name__ == '__main__':
    main()
