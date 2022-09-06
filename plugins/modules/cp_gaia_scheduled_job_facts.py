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
module: cp_gaia_scheduled_job_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show scheduled job information.
short_description: Show scheduled job/s information.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  name:
    description: Scheduled job name to show. If not specified, all scheduled jobs information is returned.
    required: false
    type: str

"""

EXAMPLES = """
- name: Show scheduled jobs
  check_point.gaia.cp_gaia_scheduled_job_facts:

- name: Show scheduled job by specifying it's name
  check_point.gaia.cp_gaia_scheduled_job_facts):
    name: test_job

"""

RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        jobs:
            description: All jobs.
            returned: always
            type: list
            elements: dict
            contains:
                name:
                    description: Scheduled job name.
                    returned: always
                    type: str
                command:
                    description: Command (expert CLI style).
                    returned: always
                    type: str
                recurrence:
                    description: Recurrence.
                    returned: always
                    type: dict
                    contains:
                        type:
                            description: Job recurrence type.
                            returned: always
                            type: str
                        interval:
                            description: Time interval in minutes. Relevant for "interval" recurrence type.
                            returned: always
                            type: int
                        time_of_day:
                            description: Time of day in 24 hour format. Relevant for "daily", "weekly" and "monthly" recurrence types.
                            returned: always
                            type: dict
                            contains:
                                hour:
                                    description: Time hour.
                                    returned: always
                                    type: int
                                minute:
                                    description: Time minute.
                                    returned: always
                                    type: int
                        hourly:
                            description: Hours of day in 24 hour format. Can choose multiple hours. Relevant for "hourly" recurrence type.
                            returned: always
                            type: dict
                            contains:
                                hours_of_day:
                                    description: Hours of day in 24 hour format.
                                    returned: always
                                    type: list
                                    elements: int
                                minute:
                                    description: Time minute.
                                    returned: always
                                    type: int
                        weekdays:
                            description: Days of the week. Relevant for "weekly" recurrence type.
                            returned: always
                            type: list
                            elements: str
                        days:
                            description: Days of the month. Relevant for "monthly" recurrence type.
                            returned: always
                            type: list
                            elements: int
                        months:
                            description: Month numbers. Relevant for "monthly" recurrence type.
                            returned: always
                            type: list
                            elements: int
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict(
        name=dict(required=False, type='str')
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'scheduled-job'
    gaia_api_version = 'v1.7/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, True)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
