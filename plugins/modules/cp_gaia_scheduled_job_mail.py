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
module: cp_gaia_scheduled_job_mail
author: Ameer Asli (@chkp-ameera)
description:
- Set which e-mail address the job scheduler sends reports to. Pass empty string to delete the current e-mail address.
short_description: Modify scheduled job mail.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
  email_address:
    description: E-mail address to send reports to.
    required: True
    type: str
"""

EXAMPLES = """
- name: Set scheduled job mail
  check_point.gaia.cp_gaia_scheduled_job_mail:
    email_address: "sysadmins@company.com"

"""

RETURN = """
scheduled_job_mail:
  description: The updated scheduled job mail.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        email_address=dict(required=True, type='str')
    )

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'scheduled-job-mail'
    gaia_api_version = 'v1.7/'

    res = chkp_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
