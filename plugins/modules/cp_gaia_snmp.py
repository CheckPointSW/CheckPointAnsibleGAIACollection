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
- SNMP agent configuration.
module: cp_gaia_snmp
short_description: SNMP agent configuration.
version_added: '6.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    version:
      description: Gaia API version for example 1.6.
      required: False
      type: str
    virtual_system_id:
      description: Virtual System ID.
      required: False
      type: int
    enabled:
        description: Enables/Disables the SNMP Agent.
        required: False
        type: bool
    ver:
        description: Configures the supported SNMP version v1, v2 and v3.
        required: False
        type: str
        choices: [any, v3-only]
    trap_usm:
        description: The user which will generate the SNMP traps, should be existed usm user
        required: False
        type: str
    contact:
        description: SNMP contact string
        required: False
        type: str
    location:
        description: SNMP location string Specifies a string that contains the location for the device.
        required: False
        type: str
    read_only_community:
        description: SNMP read-only community password, Where read-only lets you only read the values of SNMP objects
        required: False
        type: str
    read_write_community:
        description: SNMP read-write community password, Where read-write read and set the values as well
        required: False
        type: str
    interfaces:
        description: Adds a local interface to the list of local interfaces, on which the SNMP daemon listens
        required: False
        type: str
    pre_defined_traps_settings:
        description:
          - Pre-defined traps settings.
        type: dict
        suboptions:
            polling_frequency:
                description:
                  - Polling interval in seconds
                type: int
    custom_traps_settings:
        description:
          - Custom traps settings.
        type: dict
        suboptions:
            clear_trap_interval:
                description:
                  - Interval in second between clear traps
                type: int
            clear_trap_amount:
                description:
                  - Number of clear traps that is sent after custom trap termination
                type: int
    vsx_settings:
        description:
          - VSX settings.
        type: dict
        suboptions:
            enabled:
                description:
                  - True if SNMP is in vsx mode
                type: bool
            vs_access:
                description:
                  - SNMP vs-access type direct/indirect queries on Virtual-Devices
                  - direct- SNMP direct queries on Virtual-Devices
                  - indirect- SNMP direct queries via VS0
                type: str
                choices: [direct, indirect]
            sysname:
                description:
                  - This command is relevant only for VSX with SNMP VS mode, Where
                  - False = the sysname OID for all Virtual Devices will return the same result VS0 hostname
                  - True = VS0 sysname OID returns the VSX hostname and Virtual Device sysname OID returns the Check Point object name of the Virtual Device
                type: bool
"""


EXAMPLES = """
- name: Set SNMP status
  check_point.gaia.cp_gaia_snmp:
    enabled: true

"""


RETURN = """
snmp:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type="bool"),
        ver=dict(type="str", choices=["any", "v3-only"]),
        trap_usm=dict(type="str", required=False),
        contact=dict(type="str", required=False),
        location=dict(type="str", required=False),
        read_only_community=dict(type="str", required=False),
        read_write_community=dict(type="str", required=False),
        interfaces=dict(type="str", required=False),
        pre_defined_traps_settings=dict(
            type="dict",
            options=dict(polling_frequency=dict(type="int"))
        ),
        custom_traps_settings=dict(
            type="dict",
            options=dict(
                clear_trap_interval=dict(type="int"),
                clear_trap_amount=dict(type="int")
            )
        ),
        vsx_settings=dict(
            type="dict",
            options=dict(
                enabled=dict(type="bool"),
                vs_access=dict(type="str", choices=["direct", "indirect"]),
                sysname=dict(type="bool")
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'snmp'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
