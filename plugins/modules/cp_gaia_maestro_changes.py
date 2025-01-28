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

DOCUMENTATION = '''
---
author: Roi Tal (@chkp-roital)
description: Handle pending changes, either apply or delete them.
module: cp_gaia_maestro_changes 
short_description: Handle pending changes, either apply or delete them.
version_added: '7.0.0'
requirements: ['supported starting from gaia_api >= 1.8']
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  state:
    description: Ansible state which can be C(present) or C(absent). absent will delete the pending changes, present will apply them
    required: False
    type: str
    default: present
    choices: [present, absent]
notes:
- Supports C(check_mode).
'''

EXAMPLES = """
- name: Delete pending changes
  check_point.gaia.cp_gaia_user:
    state: absent

"""

RETURN = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent'])
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "maestro-security-groups-changes"

    res = chkp_api_call(module, api_call_object, False, is_maestro_special=True)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
