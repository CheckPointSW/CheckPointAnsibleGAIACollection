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
- Show the NTP state, servers(primary and secondary) and the current NTP server.
module: cp_gaia_ntp_facts
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
short_description: Show NTP settings.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6


"""


EXAMPLES = """
- name: Show current NTP configuration
  check_point.gaia.cp_gaia_ntp_facts:


"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        enabled:
            description: active status.
            returned: always
            type: bool
        servers:
            description: Servers list.
            returned: always
            type: list
            elements: dict
            contains:
                address:
                    description: Ipv4-address or Ipv6-address.
                    returned: always
                    type: str
                version:
                    description: NTP version.
                    returned: always
                    type: int
                type:
                    description: NTP type.
                    returned: always
                    type: str
                status:
                    description: NTP status.
                    returned: always
                    type: str
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict()
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ntp'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
