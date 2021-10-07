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
author: Majd Sharkia (@chkp-majds)
description:
- Setting system logging configuration
module: cp_gaia_syslog
short_description: Setting system logging configuration
version_added: '2.0.0'
requirements:
- supported starting from gaia_api >= 1.7
options:

    send_to_mgmt:
        description: sending logs to Management server
        required: False
        type: bool
    cp_logs:
        description: syslog auditlog permanent
        required: False
        type: bool
    audit_log:
        description: syslog auditlog permanent
        required: False
        type: bool
    filename:
        description: syslog output filename
        required: False
        type: str

"""


EXAMPLES = """
- name: Modify system logging configuration
  cp_gaia_syslog:
    "send_to_mgmt": false
    "filename": "/var/log/messages"
    "cp_logs": false
    "audit_log": true

"""


RETURN = """
syslog:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        send_to_mgmt=dict(type="bool"),
        cp_logs=dict(type="bool"),
        audit_log=dict(type="bool"),
        filename=dict(type="str")
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-syslog'
    ansible_release_version = 'v1.6/'

    res = chkp_api_call(module, api_call_object, ansible_release_version)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
