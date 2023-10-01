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
- Show the time and date configuration.
module: cp_gaia_time_and_date
short_description: Show the time and date configuration.
version_added: '5.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
options:
    version:
      description: Gaia API version for example 1.7.
      required: False
      type: str
    time:
      description: Time to set, in HH:MM[:SS] format.
      required: False
      type: str
    date:
      description: Date to set, in YYYY-MM-DD format.
      required: False
      type: str
    timezone:
      description: Timezone in Area / Region format. See timezone list via cp_gaia_timezones_facts.
      required: False
      type: str
    wait_for_task:
      description: Wait for task or return immediately.
      required: False
      default: True
      type: bool
"""


EXAMPLES = """
- name: Setting new time and date
  check_point.gaia.cp_gaia_time_and_date:
    time: newpass
    date: newpass
    timezone: newpass
"""


RETURN = """
set_time_and_date:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async


def main():
    # arguments for the module:
    fields = dict(
        time=dict(type='str'),
        date=dict(type='str'),
        timezone=dict(type='str')
    )
    fields.update(checkpoint_argument_spec_for_async)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-time-and-date'

    # Run the command:
    res = chkp_api_operation(module, api_call_object)

    module.exit_json(**res)


if __name__ == "__main__":
    main()
