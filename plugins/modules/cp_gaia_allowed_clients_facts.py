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
- Show the configuration of allowed clients.
module: cp_gaia_allowed_clients_facts
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  virtual_system_id:
      description: Virtual System ID.
      required: False
      type: int
short_description: Show the configuration of allowed clients.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
"""


EXAMPLES = """
- name: Show allowed clients
  check_point.gaia.cp_gaia_allowed_clients_facts:
"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        allowed_any_host:
            description:
              - Allowed any host to access the server.
            returned: always
            type: bool
        allowed_hosts:
            description:
              - Lists of allowed hosts.
            returned: always
            type: list
            elements: str
        allowed_networks:
            description:
              - List of allowed networks.
            returned: always
            type: list
            elements: dict
            contains:
              subnet:
                description: The network subnet.
                type: str
              mask_length:
                description: The network mask length.
                type: int
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict()
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    api_call_object = 'allowed-clients'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
