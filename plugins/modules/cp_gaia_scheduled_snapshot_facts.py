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
- Show the snapshot scheduler configuration.
module: cp_gaia_scheduled_snapshot_facts
short_description: Show the snapshot scheduler configuration.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
"""


EXAMPLES = """
- name: Show the snapshot scheduler configuration
  check_point.gaia.cp_gaia_scheduled_snapshot_facts:
"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        description:
                description: Description of the scheduled snapshot.
                returned: always
                type: str
        enabled:
                description: State of the snapshot scheduler.
                returned: always
                type: bool
        retention_policy:
                description: Retention policy for the snapshot scheduler.
                returned: always
                type: dict
                contains:
                    keep_disk_space_above_in_GB:
                        description: Minimum diskspace to keep on the local machine (GB).
                        returned: always
                        type: int
                    min_snapshots_to_keep:
                        description: Minimum snapshots to keep.
                        returned: always
                        type: int
                    max_snapshots_to_keep:
                        description: Maximum snapshots to keep.
                        returned: always
                        type: int
        recurrence:
                description: Recurrence of the scheduled snapshot.
                returned: always
                type: dict
                contains:
                    time:
                        description: Recurrence time.
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
                    pattern:
                        description: Recurrence pattern. choices=['daily', 'monthly', 'weekly'].
                        returned: always
                        type: str
                    months:
                        description: Recurrence months.
                        returned: always
                        type: list
                        elements: int
                    weekdays:
                        description: Recurrence weekdays.
                        returned: always
                        type: list
                        elements: str
                    days:
                        description: Recurrence days.
                        returned: always
                        type: list
                        elements: int
        name_prefix:
              description: Prefix for the snapshots name created by the scheduler.
              returned: always
              type: str
        host:
              description: Target host for the snapshots creation.
              returned: always
              type: dict
              contains:
                    username:
                        description: Username for scp/ftp targets.
                        returned: always
                        type: str
                    upload_path:
                        description: Upload path for scp/ftp targets.
                        returned: always
                        type: str
                    password:
                        description: Password for scp/ftp targets.
                        returned: always
                        type: str
                    target:
                        description: Host target type. choices=['lvm', 'ftp', 'scp'].
                        returned: always
                        type: str
                    ip_address:
                        description: IP_Address of the target.
                        returned: always
                        type: str
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict()
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    api_call_object = 'scheduled-snapshot'
    gaia_api_version = 'v1.6/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
