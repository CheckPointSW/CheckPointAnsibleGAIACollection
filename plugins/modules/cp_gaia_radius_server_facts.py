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
- Show radius servers settings.
module: cp_gaia_radius_server_facts
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
short_description: Show radius servers settings.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
"""


EXAMPLES = """
- name: Show radius servers settings.
  check_point.gaia.cp_gaia_radius_server_facts:
"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        super_user_uid:
            description: The UID that will be given to a super user.
            returned: always
            type: str
        default_shell:
            description: Default shell when login.
            returned: always
            type: str
        nas_ip:
            description: The NAS IP for the radius client.
            returned: always
            type: str
        servers:
            description: Radius servers list.
            returned: always
            type: list
            elements: dict
            contains:
                priority:
                    description: Search priority (lower values comes first). Valid values are -999 - 999.
                    returned: always
                    type: int
                secret:
                    description: Secret string.
                    returned: always
                    type: str
                port:
                    description: UDP port to contact on the RADIUS server.
                    returned: always
                    type: int
                timeout:
                    description: Valid values are 1-50.
                    returned: always
                    type: int
                address:
                    description: Server address.
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

    api_call_object = 'radius'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
