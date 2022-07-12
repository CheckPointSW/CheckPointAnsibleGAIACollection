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
module: cp_gaia_scheduled_job
author: Ameer Asli (@chkp-ameera)
description:
- Change the scheduled job's recurrence or command. Scheduled jobs run as admin.
short_description: Modify scheduled job.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  state:
    description: Ansible state which can be C(present) or C(absent).
    required: False
    type: str
    default: present
    choices: [present, absent]
  name:
    description: Scheduled job name.
    required: True
    type: str
  command:
    description: Command (expert CLI style).
    required: False
    type: str
  recurrence:
    description: Recurrence.
    required: False
    type: dict
    suboptions:
        type:
            description: Job recurrence type.
            required: False
            type: str
            choices: ['system-startup', 'interval', 'hourly', 'daily', 'weekly', 'monthly']
        interval:
            description: Time interval in minutes. Relevant for "interval" recurrence type.
            required: False
            type: int
        time_of_day:
            description: Time of day in 24 hour format. Relevant for "daily", "weekly" and "monthly" recurrence types.
            required: False
            type: dict
            suboptions:
                hour:
                    description: Time hour.
                    required: False
                    type: int
                minute:
                    description: Time minute.
                    required: False
                    type: int
        hourly:
            description: Hours of day in 24 hour format. Can choose multiple hours. Relevant for "hourly" recurrence type.
            required: False
            type: dict
            suboptions:
                hours_of_day:
                    description: Hours of day in 24 hour format.
                    required: False
                    type: list
                    elements: int
                minute:
                    description: Time minute.
                    required: False
                    type: int
        weekdays:
            description: Days of the week. Relevant for "weekly" recurrence type.
            required: False
            type: list
            elements: str
        days:
            description: Days of the month. Relevant for "monthly" recurrence type.
            required: False
            type: list
            elements: int
        months:
            description: Month numbers. Relevant for "monthly" recurrence type.
            required: False
            type: list
            elements: int
"""

EXAMPLES = """
- name: Add new scheduled job
  check_point.gaia.cp_gaia_scheduled_job:
    name: "startup_job"
    command: "/home/admin/job.sh"
    recurrence: {"type": "system-startup"}

"""

RETURN = """
scheduled_job:
  description: The updated scheduled job details.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(required=True, type='str'),
        command=dict(type='str'),
        recurrence=dict(
            type='dict',
            options=dict(
                type=dict(type='str', choices=['system-startup', 'interval', 'hourly', 'daily', 'weekly', 'monthly']),
                interval=dict(type='int'),
                time_of_day=dict(
                    type='dict',
                    options=dict(
                        hour=dict(type='int'),
                        minute=dict(type='int')
                    )
                ),
                hourly=dict(
                    type='dict',
                    options=dict(
                        hours_of_day=dict(type='list', elements='int'),
                        minute=dict(type='int')
                    )
                ),
                weekdays=dict(type='list', elements='str'),
                days=dict(type='list', elements='int'),
                months=dict(type='list', elements='int')
            )
        )
    )

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'scheduled-job'
    gaia_api_version = 'v1.7/'
    show_params = ['name']

    res = chkp_api_call(module, gaia_api_version, api_call_object, True, show_params=show_params)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
