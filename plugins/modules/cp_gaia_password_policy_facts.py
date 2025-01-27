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
- Show password policy configuration.
module: cp_gaia_password_policy_facts
options:
  version:
    description: Gaia API version for example 1.6.
    required: False
    type: str
  virtual_system_id:
    description: Virtual System ID.
    required: False
    type: int
short_description: Show password policy configuration.
version_added: '3.0.0'
notes:
- Supports C(check_mode).
requirements:
- supported starting from gaia_api >= 1.6
"""


EXAMPLES = """
- name: Show password policy configuration
  check_point.gaia.cp_gaia_password_policy_facts:
"""


RETURN = """
ansible_facts:
    description: The checkpoint object facts.
    returned: always.
    type: dict
    contains:
        lock_settings:
            description: Password change configuration.
            returned: always
            type: dict
            contains:
                inactivity_settings:
                    description: Inactivity configuration.
                    returned: always
                    type: dict
                    contains:
                        lock_unused_accounts_enabled:
                            description: Password lock unused accounts.
                            returned: always
                            type: bool
                        inactivity_threshold_days:
                            description: Inactivity days to password expiration lockout, Valid values are 1-1827.
                            returned: always
                            type: int
                failed_attempts_settings:
                    description: Failed attempts configuration.
                    returned: always
                    type: dict
                    contains:
                        failed_lock_duration_seconds:
                            description: Password failed logging lockout duration, Valid values are 60-604800.
                            returned: always
                            type: int
                        failed_lock_enforced_on_admin:
                            description: Enforce failed lockout on admin user.
                            returned: always
                            type: bool
                        failed_lock_enabled:
                            description: Lock user after exceeded maximum allowed login attempts.
                            returned: always
                            type: bool
                        failed_attempts_allowed:
                            description: Amount of login attempts allowed before lockout, Valid values are 2-1000.
                            returned: always
                            type: int
                password_expiration_days:
                    description: Password expiration lifetime, Valid values are 60-604800.
                    returned: always
                    type: int
                password_expiration_warning_days:
                    description: Number of days before a password expires that the user gets warned, Valid values are 1-366.
                    returned: always
                    type: int
                password_expiration_maximum_days_before_lock:
                    description: Password expiration lockout in days, Valid values are 1-1827.
                    returned: always
                    type: int
                must_one_time_password_enabled:
                    description: Forces a user to change their password after it has been set via "User Management"
                                 (but not via "Self Password Change" or forced change at login).
                                 Use this command to set the value.
                    returned: always
                    type: bool
        password_history:
            description: Password history configuration.
            returned: always
            type: dict
            contains:
                check_history_enabled:
                    description: Password history check.
                    returned: always
                    type: bool
                repeated_history_length:
                    description: Password history length.
                    returned: always
                    type: int
        password_strength:
            description: Password history configuration.
            returned: always
            type: dict
            contains:
                minimum_length:
                    description: Password minimum length, Valid values are 6-128.
                    returned: always
                    type: int
                complexity:
                    description: Password complexity, Valid values are 1-4.
                    returned: always
                    type: int
                palindrome_check_enabled:
                    description: Password palindrome check.
                    returned: always
                    type: bool
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict()
    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    api_call_object = 'password-policy'

    res = chkp_facts_api_call(module, api_call_object, False)
    module.exit_json(ansible_facts=res["ansible_facts"])


if __name__ == "__main__":
    main()
