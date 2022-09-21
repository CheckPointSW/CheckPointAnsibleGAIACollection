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
module: cp_gaia_ssh_server_settings_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show SSH server settings, request only supported on GAIA versions R81.20+.
short_description: Show SSH server settings.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  include_disabled_values:
    description: Include disabled algorithms.
    required: False
    type: bool
    default: False

"""

EXAMPLES = """
- name: Show SSH server settings
  check_point.gaia.cp_gaia_ssh_server_settings_facts:

"""

RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        enabled_ciphers:
            description: Enabled ssh ciphers.
            returned: always.
            type: list
            elements: str
        enabled_mac_algorithms:
            description: Enabled ssh mac algorithms.
            returned: always.
            type: list
            elements: str
        enabled_kex_algorithms:
            description: Enabled ssh kex algorithms.
            returned: always.
            type: list
            elements: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        include_disabled_values=dict(type='bool', default=False)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ssh-server-settings'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
