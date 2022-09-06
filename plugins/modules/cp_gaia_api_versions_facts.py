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
module: cp_gaia_api_versions_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show api versions.
short_description: Show api versions.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
"""

EXAMPLES = """
- name: Show api versions
  check_point.gaia.cp_gaia_api_versions_facts:
"""

RETURN = """
ansible_facts:
    description: The api versions facts.
    returned: always.
    type: dict
    contains:
        current_version:
            description:
              - Represents the latest supported version by the installed REST engine.
            returned: always
            type: str
        supported_versions:
            description:
              - Represents all the previous versions supported by the installed REST engine.
            returned: always
            type: list
            elements: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict()
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'api-versions'
    gaia_api_version = 'v1.6/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
