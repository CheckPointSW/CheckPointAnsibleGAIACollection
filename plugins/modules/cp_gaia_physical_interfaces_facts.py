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
module: cp_gaia_physical_interfaces_facts
author: Yuval Feiger (@chkp-yuvalfe)
description:
- Show Physical interfaces.
short_description: Show Physical interface/s.
version_added: '1.0.0'
notes:
- Supports C(check_mode).
options:
  name:
    description: Interface name to show. If not specified, all physical interfaces information is returned.
    required: false
    type: str

"""

EXAMPLES = """
- name: Show physical interfaces
  check_point.gaia.cp_gaia_physical_interfaces_facts:

- name: Show physical interface by specifying it name
  check_point.gaia.cp_gaia_physical_interfaces_facts:
    name: eth0

"""

RETURN = """
ansible_facts:
  description: The interface/s facts.
  returned: always.
  type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict(
        name=dict(required=False, type="str")
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "physical-interface"
    gaia_api_version = 'v1.6/'
    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
