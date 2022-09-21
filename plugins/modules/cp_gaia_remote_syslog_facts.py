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
author: Majd Sharkia (@chkp-majds)
description:
- Show remote system log server configuration.
module: cp_gaia_remote_syslog_facts
short_description: Show remote system log server configuration.
version_added: '2.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    version:
        description: Gaia API version for example 1.6.
        required: False
        type: str
    server_ip:
        description: No Documentation available.
        required: False
        type: str

"""


EXAMPLES = """
- name: Show remote syslog log server by specifying it IP
  check_point.gaia.cp_gaia_remote_syslog_facts:
    server_ip: "10.11.2.130"

"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        server_ip:
            description: No Documentation available.
            returned: always
            type: str
        state:
            description: Ansible state which can be C(present) or C(absent).
            returned: always
            type: str
        protocol:
            description: Log protocol, Supported starting from R81.20 .
            returned: always
            type: str
        port:
            description: Log port, Supported starting from R81.20 .
            returned: always
            type: str
        level:
            description: No Documentation available.
            returned: always
            type: str
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        server_ip=dict(type="str")
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'remote-syslog'

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
