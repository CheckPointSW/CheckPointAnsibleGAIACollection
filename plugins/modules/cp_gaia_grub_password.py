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
- Sets GRUB password.
module: cp_gaia_grub_password
short_description: Sets GRUB password.
version_added: '6.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.7
options:
    version:
      description: Gaia API version for example 1.7.
      required: False
      type: str
    virtual_system_id:
      description: Virtual System ID.
      required: False
      type: int
    password:
        description: GRUB new password.
        required: False
        type: str
    password_hash:
        description: An encrypted representation of the password.
        required: False
        type: str
"""


EXAMPLES = """
- name: Setting GRUB new password
  check_point.gaia.cp_gaia_grub_password:
    password: newpass
"""


RETURN = """
grub_password:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        password=dict(type='str', no_log=True),
        password_hash=dict(type='str', no_log=True)
    )
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'grub-password'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
