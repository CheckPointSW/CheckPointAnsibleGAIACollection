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
module: cp_gaia_maestro_sites_facts
author: Roi Tal (@chkp-roital)
description:
- Show information regarding sites.
short_description: Show site/s.
version_added: "7.0.0"
notes:
- Supports C(check_mode).
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  site_id:
    description: ID of site to show. If not specified, all sites information is returned.
    required: false
    type: int
  include_pending_changes:
    description: If true, show pending topology. If false, show deployed topology
    required: False
    type: bool
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
"""

EXAMPLES = """
- name: Show Maestro sites
  check_point.gaia.cp_gaia_site_facts:

- name: Show site 1
  check_point.gaia.cp_gaia_site_facts:
    site_id: 1
"""

RETURN = """
ansible_facts:
    description: The Maestro site/s facts.
    returned: always.
    type: dict
    contains:
        gateways:
            description:
              - List of sites.
            returned: always
            type: list
            elements: dict
            contains:
                site_id:
                    description:
                      - Site ID.
                    returned: always
                    type: int
                descriptions:
                    description:
                      - List of this Site descriptions in different Security Groups.
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        security_group:
                            description: The site Security Group
                            type: int
                            returned: always
                        description:
                            description: Site description
                            type: str
                            returned: always
                gateways:
                    description:
                      - List of Maestro Gateways.
                    returned: always
                    type: list
                    elements: dict
                    contains:
                        id:
                            description:
                              - Maestro Gateway ID.
                            returned: always
                            type: str
                        site:
                            description:
                              - Site this Gateway belongs to.
                            returned: always
                            type: int
                        security_group:
                            description:
                              - The Security Group this Gateway belongs to.
                            returned: always
                            type: int
                        member_id:
                            description:
                              - The member ID of this Gateway, if it's assigned to a Security Group.
                            returned: always
                            type: int
                        model:
                            description:
                              - Model of this Gateway.
                            returned: always
                            type: str
                        version:
                            description:
                              - OS version installed on this Gateway.
                            returned: always
                            type: dict
                            contains:
                                major:
                                    description:
                                      - Major version
                                    returned: always
                                    type: str
                        downlink_ports:
                            description:
                              - The Orchestrator ports which are connected to the Gateway.
                            returned: always
                            type: list
                            elements: dict
                            contains:
                                orchestrator_id:
                                    description:
                                      - ID of the Orchestrator to which this port belongs
                                    returned: always
                                    type: str
                                port:
                                    description:
                                      - Port ID
                                    returned: always
                                    type: str
                        description:
                            description:
                              - Description of this Gateway.
                            returned: always
                            type: str
                        state:
                            description:
                              - State of this Gateway.
                            returned: always
                            type: str
                        weight:
                            description:
                              - Weight assigned to this Gateway, in case it's assigned to a Security Group.
                            returned: always
                            type: int
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        include_pending_changes=dict(required=False, type='bool'),
        site_id=dict(required=False, type='int')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "maestro-site"

    res = chkp_facts_api_call(module, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
