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
author: Ophir Khill (@chkp-ophirk)
description:
- Installing policy
module: cp_gaia_dynamic_content
options:
    version:
        description: GAIA api version for ex 1.8
        required: False
        type: str
    policy_path:
        description: path for the policy json
        required: True
        type: str
    dry_run:
        description: dry_run set to true will apply the change, wheres set to false it will only validate the changes
        required: True
        type: bool
    tags:
        description: list of tags for the operation
        required: True
        type: list
        elements: str
    comments:
        description: comments for the operation
        required: True
        type: str
    wait_for_task:
        description: Wait for task or return immediately.
        required: False
        default: false
        type: bool
short_description: installing policy
version_added: '5.1.0'
notes:
- its advisable to perform with wait_for_task set to false and refer to show_task command
"""

EXAMPLES = """
- name: Initial setup
  check_point.gaia.cp_gaia_dynamic_content:
    policy_path: "/home/admin/policy.json"
    dry_run: false
    tags: ["JIRA-12345", "apply layer1"]
    comments: "testing the api"
    wait_for_task: true
"""

RETURN = """
change_summary:
  description: change-summary after installing the new policy.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_all
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_async_false
import json

NO_CHANGES = \
    {
        "layers": [],
        "objects": {
            "create": [],
            "delete": [],
            "modify": []
        }
    }

KEYS_TO_REMOVE = ['comments', 'tags', 'dry-run']


# load json
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # remove unnecessary arguments
            for key in KEYS_TO_REMOVE:
                data.pop(key, None)

            return data, None
    except Exception as e:
        return None, str(e)


# check if the policy has changed
def has_changed(result):
    changed = True
    change_summary = {}

    try:
        change_summary = result['set_dynamic_content']['tasks'][0]['task-details'][0]['change-summary']
    except KeyError:
        # no change summary
        return changed

    if change_summary == NO_CHANGES:
        changed = False

    return changed


def main():
    # arguments for the module:
    fields = {
        'policy_path': dict(type='str', required=True),
        'dry_run': dict(type='bool', required=True),
        'comments': dict(type='str', required=True),
        'tags': dict(type='list', elements='str', required=True)
    }
    fields.update(checkpoint_argument_spec_for_async_false)
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    file_path = module.params['policy_path']

    # load policy
    result, error = load_json_file(file_path)
    if error:
        module.exit_json(changed=False, json_data=result)

    # add policy to request
    del module.params['policy_path']
    module.params.update(result)
    # call api operation
    api_call_object = "set-dynamic-content"
    res = chkp_api_operation(module, api_call_object)
    # fill in 'changed' field
    res['changed'] = has_changed(res)

    module.exit_json(**res)


if __name__ == "__main__":
    main()
