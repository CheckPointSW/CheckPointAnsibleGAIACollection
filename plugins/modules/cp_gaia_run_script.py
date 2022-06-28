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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = """
author: Ameer Asli (@chkp-ameera)
description:
- run script on Check Point machine.
module: cp_gaia_run_script
options:
  script:
    description: Script body. Limited by 1300000 characters
    required: True
    type: str
  description:
    description: Script description
    required: False
    type: str
  args:
    description: Script arguments, separated by space character. Note don't send sensitive data on this parameter.
    required: False
    type: str
  environment_variables:
      description: Define environment variables to be used in the script, it's better to send sensitive data on environment variables since it's not stored.
      required: False
      type: list
      elements: dict
      suboptions:
        name:
          description: Variable's name
          required: False
          type: str
        value:
          description: Variable's value
          required: False
          type: str
  wait_for_task:
    description: wait for task or return immediately
    required: False
    default: True
    type: bool
short_description: run script Check Point machine.
version_added: '3.0.0'

"""


EXAMPLES = """
- name: run script
  cp_gaia_run_script:
    script: "ls -la"
    environment_variables: [{"name": "VAR_NAME", "value": "VAR_VALUE"}]
"""

RETURN = """
run_script:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_operation, checkpoint_argument_spec_for_async


def main():
    # arguments for the module:
    fields = dict(
        script=dict(type='str', required=True),
        description=dict(type='str'),
        args=dict(type='str'),
        environment_variables=dict(
            type='list', elements='dict',
            options=dict(
                name=dict(type='str'),
                value=dict(type='str')
            )
        ),
    )
    fields.update(checkpoint_argument_spec_for_async)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'run-script'
    gaia_api_version = 'v1.6/'

    # Run the command:
    res = chkp_api_operation(module, gaia_api_version, api_call_object)

    module.exit_json(**res)


if __name__ == "__main__":
    main()
