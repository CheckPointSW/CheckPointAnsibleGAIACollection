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
module: cp_gaia_alias_interface_facts
author: Duane Toler (@duanetoler)
description:
- Show alias interface.
short_description: Show alias interface/s.
version_added: '8.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  name:
    description: Interface name to show. If not specified, all alias interfaces information is returned.
    required: false
    type: str
"""

EXAMPLES = """
- name: Show alias interface
  check_point.gaia.cp_gaia_alias_interface_facts:
- name: Show alias interface by specifying it's name
  check_point.gaia.cp_gaia_alias_interface_facts:
    name: eth0:1
"""

RETURN = """
ansible_facts:
    description: The interface/s facts.
    returned: always.
    type: dict
    contains:
        objects:
            description:
              - List of interfaces.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description:
                      - Interface name.
                    returned: always
                    type: str
                ipv4_address:
                    description: Interface IPv4 address.
                    returned: always
                    type: str
                ipv4_mask_length:
                    description: Interface IPv4 address mask length.
                    returned: always
                    type: int
                enabled:
                    description: Interface State.
                    returned: always
                    type: bool
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        name=dict(required=False, type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "alias-interface"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()