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
- Set scheduled snapshot.
module: cp_gaia_scheduled_snapshot
short_description: Set scheduled snapshot.
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
  description:
        description: Description of the scheduled snapshot.
        required: False
        type: str
  enabled:
        description: State of the snapshot scheduler.
        required: False
        type: bool
  retention_policy:
        description: Retention policy for the snapshot scheduler.
        required: False
        type: dict
        suboptions:
            keep_disk_space_above_in_GB:
                description: Minimum diskspace to keep on the local machine (GB).
                required: False
                type: int
            min_snapshots_to_keep:
                description: Minimum snapshots to keep.
                required: False
                type: int
            max_snapshots_to_keep:
                description: Maximum snapshots to keep.
                required: False
                type: int
  recurrence:
        description: Recurrence of the scheduled snapshot.
        required: False
        type: dict
        suboptions:
            time:
                description: Recurrence time.
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
            pattern:
                description: Recurrence pattern. choices=['daily', 'monthly', 'weekly'].
                required: False
                type: str
                choices: ['daily', 'monthly', 'weekly']
            months:
                description: Recurrence months.
                required: False
                type: list
                elements: int
            weekdays:
                description: Recurrence weekdays.
                required: False
                type: list
                elements: str
            days:
                description: Recurrence days.
                required: False
                type: list
                elements: int
  name_prefix:
      description: Prefix for the snapshots name created by the scheduler.
      required: False
      type: str
  host:
      description: Target host for the snapshots creation.
      required: False
      type: dict
      suboptions:
            username:
                description: Username for scp/ftp targets.
                required: False
                type: str
            upload_path:
                description: Upload path for scp/ftp targets.
                required: False
                type: str
            password:
                description: Password for scp/ftp targets.
                required: False
                type: str
            target:
                description: Host target type. choices=['lvm', 'ftp', 'scp'].
                required: False
                type: str
                choices: ['lvm', 'ftp', 'scp']
            ip_address:
                description: IP_Address of the target.
                required: False
                type: str
"""


EXAMPLES = """
- name: Set scheduled snapshot
  check_point.gaia.cp_gaia_scheduled_snapshot:
    recurrence: {"pattern": "weekly", "weekdays": ["Mon","Wed"], time: {"minute": 30,"hour": 13}}
    name_prefix: "weeklySnap"
    host: {"username": "username","upload_path": "/home/admin/", "password": "secret", "target": "lvm"}
    enabled: True
    description: "weekly"
"""


RETURN = """
scheduled_snapshot:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        description=dict(type='str'),
        enabled=dict(type='bool'),
        retention_policy=dict(
            type='dict',
            options=dict(
                keep_disk_space_above_in_GB=dict(type='int'),
                min_snapshots_to_keep=dict(type='int'),
                max_snapshots_to_keep=dict(type='int')
            )
        ),
        recurrence=dict(
            type='dict',
            options=dict(
                time=dict(
                    type='dict',
                    options=dict(
                        hour=dict(type='int'),
                        minute=dict(type='int')
                    )
                ),
                pattern=dict(type='str', choices=['daily', 'monthly', 'weekly']),
                months=dict(type='list', elements='int'),
                weekdays=dict(type='list', elements='str'),
                days=dict(type='list', elements='int')
            )
        ),
        name_prefix=dict(type='str'),
        host=dict(
            type='dict',
            options=dict(
                username=dict(type='str'),
                upload_path=dict(type='str'),
                password=dict(type='str', no_log=True),
                target=dict(type='str', choices=['lvm', 'ftp', 'scp']),
                ip_address=dict(type='str'),
            )
        )
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'scheduled-snapshot'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
