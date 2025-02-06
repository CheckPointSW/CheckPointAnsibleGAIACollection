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
module: cp_gaia_snmp_pre_defined_traps
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
    authorizationError:
        description: authorizationError Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the authorizationError Trap.
                required: False
                type: bool
    biosFailure:
        description: biosFailure Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the biosFailure Trap.
                required: False
                type: bool
    configurationChange:
        description: configurationChange Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the configurationChange Trap.
                required: False
                type: bool
    configurationSave:
        description: configurationSave Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the configurationSave Trap.
                required: False
                type: bool
    fanFailure:
        description: fanFailure Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the fanFailure Trap.
                required: False
                type: bool
    highVoltage:
        description: highVoltage Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the highVoltage Trap.
                required: False
                type: bool
    linkUpLinkDown:
        description: linkUpLinkDown Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the linkUpLinkDown Trap.
                required: False
                type: bool
    clusterXLFailover:
        description: clusterXLFailover Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the clusterXLFailover Trap.
                required: False
                type: bool
    lowVoltage:
        description: lowVoltage Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the lowVoltage Trap.
                required: False
                type: bool
    overTemperature:
        description: overTemperature Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the overTemperature Trap.
                required: False
                type: bool
    powerSupplyFailure:
        description: powerSupplyFailure Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the powerSupplyFailure Trap.
                required: False
                type: bool
    raidVolumeState:
        description: raidVolumeState Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the raidVolumeState Trap.
                required: False
                type: bool
    vrrpv2AuthFailure:
        description: vrrpv2AuthFailure Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the vrrpv2AuthFailure Trap.
                required: False
                type: bool
    vrrpv2NewMaster:
        description: vrrpv2NewMaster Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the vrrpv2NewMaster Trap.
                required: False
                type: bool
    vrrpv3NewMaster:
        description: vrrpv3NewMaster Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the vrrpv3NewMaster Trap.
                required: False
                type: bool
    vrrpv3ProtoError:
        description: vrrpv3ProtoError Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the vrrpv3ProtoError Trap.
                required: False
                type: bool
    coldStart:
        description: coldStart Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the coldStart Trap.
                required: False
                type: bool
            threshold:
                description: coldStart threshold (seconds), prevents sending coldStart trap when system up-time is greater than the threshold
                required: False
                type: int
            reboot_only:
                description: ColdStart reboot only, allows sending ColdStart trap only on reboot
                required: False
                type: bool
    lowDiskSpaceAllPartitions:
        description: lowDiskSpaceAllPartitions Trap.
        required: False
        type: dict
        suboptions:
            enabled:
                description: Enables/Disables the lowDiskSpaceAllPartitions Trap.
                required: False
                type: bool
"""


EXAMPLES = """
- name: Set SNMP pre_defined traps
  check_point.gaia.cp_gaia_snmp_pre_defined_traps:
    biosFailure: {enabled: true}
"""


RETURN = """
snmp_pre_defined_traps:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        authorizationError=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        biosFailure=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        configurationChange=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        configurationSave=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        fanFailure=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        highVoltage=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        linkUpLinkDown=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        clusterXLFailover=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        lowVoltage=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        overTemperature=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        powerSupplyFailure=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        raidVolumeState=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        vrrpv2AuthFailure=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        vrrpv2NewMaster=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        vrrpv3NewMaster=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        vrrpv3ProtoError=dict(type="dict", options=dict(enabled=dict(type="bool"))),
        coldStart=dict(type="dict", options=dict(enabled=dict(type="bool"), threshold=dict(type="int"), reboot_only=dict(type="bool"))),
        lowDiskSpaceAllPartitions=dict(type="dict", options=dict(enabled=dict(type="bool")))

    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'snmp-pre-defined-traps'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
