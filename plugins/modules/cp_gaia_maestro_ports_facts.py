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
module: cp_gaia_maestro_ports_facts
author: Roi Tal (@chkp-roital)
description:
- Show information regarding Maestro Orchestrator ports.
short_description: Show port/s.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  id:
    description: ID port to show (e.g. '1/13/1'). If both id and interface_name are not specified, all ports information is returned.
    required: False
    type: str
  interface_name:
    description: Interface name in case this port is an Uplink or MGMT interface (e.g. 'eth1-25'). If both id and interface_name are not specified, all ports information is returned.
    required: False
    type: str
"""

EXAMPLES = """
- name: Show Orchestrator ports
  check_point.gaia.cp_gaia_user_facts:

- name: Show Orchestrator port by specifying it's ID
  check_point.gaia.cp_gaia_user_facts:
    id: 1/13/1
"""

RETURN = """
ansible_facts:
    description: The Maestro port/s facts.
    returned: always.
    type: dict
    contains:
        ports:
            id:
              - List of Maestro ports.
            returned: always
            type: list
            elements: dict
            contains:
                id:
                    description:
                      - Port ID.
                    returned: always
                    type: str
                site:
                    description:
                      - Site this Port belongs to.
                    returned: always
                    type: int
                interface_name:
                    description:
                      - Interface name, in case this Port is of Uplink or Management type.
                    returned: always
                    type: str
                type:
                    description:
                      - Port type, either Uplink, Downlink, Site Sync, SSM Sync or Mgmt.
                    returned: always
                    type: str
                qsfp_mode:
                    description:
                      - Port QSFO Mode.
                    returned: always
                    type: str
                enabled:
                    description:
                      - Indicates whether this port is enabled by the user. AKA 'admin state'.
                    returned: always
                    type: bool
                link_state:
                    description:
                      - True if this Port link is up, false otherwise.
                    returned: always
                    type: bool
                auto_negotiation:
                    description:
                      - True if Auto Negotiation is up for this port, false otherwise.
                    returned: always
                    type: bool
                transceiver_state:
                    description:
                      - 'PLUGGED' or 'UNPLUGGED'.
                    returned: always
                    type: str
                operating_speed:
                    description:
                      - Operating speed of this port.
                    returned: always
                    type: int
                mtu:
                    description:
                      - MTU of this port.
                    returned: always
                    type: int
                rx_frames:
                    description:
                      - Amount of received frames of this port.
                    returned: always
                    type: int
                tx_frames:
                    description:
                      - Amount of transmitted frames of this port.
                    returned: always
                    type: int
                orchestrator_id:
                    description:
                      - Security Group ID(s) in case this port is assigned to a security-group(s). Otherwise, empty list.
                    returned: always
                    type: list
                    elements: int
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        interface_name=dict(required=False, type='str'),
        id=dict(required=False, type='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "maestro-port"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
