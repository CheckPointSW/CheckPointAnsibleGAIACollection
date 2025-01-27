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
module: cp_gaia_task_facts
author: Ameer Asli (@chkp-ameera)
description:
- Show task.
short_description: Show task.
version_added: '3.0.0'
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
    task_id:
        description: List of task ids to show.
        required: True
        type: list
        elements: str
"""

EXAMPLES = """
- name: Show task
  check_point.gaia.cp_gaia_task_facts:
    task_id: ["ccc88f8f-ee65-44d2-bdc6-797f8347f6e1"]
"""

RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        tasks:
            description: Tasks.
            returned: always
            type: list
            elements: dict
            contains:
                task_id:
                    description: ID of the task being executed.
                    returned: always
                    type: str
                last_update_time:
                    description:
                      - Last update timestamp from task's execution.
                        A task can update its status during execution.
                        Updates interval will change from one API to another.
                    returned: always
                    type: str
                progress_description:
                    description: Progress description will change between one API to another.
                    returned: always
                    type: str
                progress_percentage:
                    description: Note Percentage will be marked as 100 upon failure as well.
                    returned: always
                    type: int
                start_time:
                    description: Execution start time, in iso8601 format.
                    returned: always
                    type: str
                status_code:
                    description: HTTP return code.
                    returned: always
                    type: int
                task_name:
                    description: Request URL. For example '/run-script' for run-script tasks.
                    returned: always
                    type: str
                status:
                    description: Status.
                    returned: always
                    type: str
                task_details:
                    description: The type of object depends on the request. See 'run-script' output for example.
                    returned: always
                    type: list
                    elements: dict
                execution_time:
                    description: Time in seconds.
                    returned: always
                    type: int
                time_spent_in_queue:
                    description: Time in seconds.
                    returned: always
                    type: int
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        task_id=dict(type='list', required=True, elements='str')
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'task'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
