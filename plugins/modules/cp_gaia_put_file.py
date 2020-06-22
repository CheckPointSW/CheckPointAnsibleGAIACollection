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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import api_call

DOCUMENTATION = """
author: Yuval Feiger (@chkp-yuvalfe)
description:
- Add a new file to a Check Point machine.
module: cp_gaia_put_file
options:
  file_name:
    description: Filename include the desired path. The file will be created in the user home directory if the full path wasn't provided.
    required: true
    type: str
  text_content:
    description: Content to add to the new file.
    required: true
    type: str
  override:
    description:
      - If the file already exists, indicates whether to overwrite it.
      - Recommended value: true.
      - Note: When the value is false, if the file already exists in the system from an previous execution, it will fail.
    required: true
    type: bool
short_description: Add a new file to a Check Point machine.
version_added: '2.9'

"""


EXAMPLES = """
- name: add a file
  cp_gaia_put_file:
    file_name: "ansible_file.txt"
    text_content: "It's an ansible file."
    override: true

"""

RETURN = """
put_file:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        file_name=dict(type='str', required=True),
        text_content=dict(type='str', required=True),
        override=dict(type='bool', required=True),
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    # Run the command:
    res = api_call(module=module, api_call_object="put-file")

    was_changed = True
    module.exit_json(put_file=res, changed=was_changed)


if __name__ == "__main__":
    main()
