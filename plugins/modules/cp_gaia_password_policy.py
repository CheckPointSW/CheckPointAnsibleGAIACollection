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
- Setting password policy configuration.
module: cp_gaia_password_policy
short_description: Setting password policy configuration.
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
    lock_settings:
        description: Password change configuration.
        required: False
        type: dict
        suboptions:
            inactivity_settings:
                description: Inactivity configuration.
                required: False
                type: dict
                suboptions:
                    lock_unused_accounts_enabled:
                        description: Password lock unused accounts.
                        required: False
                        type: bool
                        default: False
                    inactivity_threshold_days:
                        description: Inactivity days to password expiration lockout, Valid values are 1-1827.
                        required: False
                        type: int
                        default: 365
            failed_attempts_settings:
                description: Failed attempts configuration.
                required: False
                type: dict
                suboptions:
                    failed_lock_duration_seconds:
                        description: Password failed logging lockout duration, Valid values are 60-604800.
                        required: False
                        type: int
                        default: 1200
                    failed_lock_enforced_on_admin:
                        description: Enforce failed lockout on admin user.
                        required: False
                        type: bool
                        default: False
                    failed_lock_enabled:
                        description: Lock user after exceeded maximum allowed login attempts.
                        required: False
                        type: bool
                        default: False
                    failed_attempts_allowed:
                        description: Amount of login attempts allowed before lockout, Valid values are 2-1000.
                        required: False
                        type: int
                        default: 10
            password_expiration_days:
                description: Password expiration lifetime, Valid values are 60-604800 or "never".
                required: False
                type: raw
            password_expiration_warning_days:
                description: Number of days before a password expires that the user gets warned, Valid values are 1-366.
                required: False
                type: int
                default: 7
            password_expiration_maximum_days_before_lock:
                description: Password expiration lockout in days, Valid values are 1-1827 or "never".
                required: False
                type: raw
            must_one_time_password_enabled:
                description: Forces a user to change their password after it has been set via "User Management"
                             (but not via "Self Password Change" or forced change at login).
                             Use this command to set the value.
                required: False
                type: bool
                default: False
    password_history:
        description: Password history configuration.
        required: False
        type: dict
        suboptions:
            check_history_enabled:
                description: Password history check.
                required: False
                type: bool
                default: False
            repeated_history_length:
                description: Password history length.
                required: False
                type: int
                default: 10
    password_strength:
        description: Password history configuration.
        required: False
        type: dict
        suboptions:
            minimum_length:
                description: Password minimum length, Valid values are 6-128.
                required: False
                type: int
                default: 6
            complexity:
                description: Password complexity, Valid values are 1-4.
                required: False
                type: int
                default: 2
            palindrome_check_enabled:
                description: Password palindrome check.
                required: False
                type: bool
                default: True
"""


EXAMPLES = """
- name: Change password policy
  check_point.gaia.cp_gaia_password_policy:
        lock_settings: {'failed_attempts_settings': {'failed_attempts_allowed': 10,
                                                     'failed_lock_duration_seconds': 1200,
                                                     'failed_lock_enabled': False,
                                                     'failed_lock_enforced_on_admin': False},
                        'inactivity_settings': {'inactivity_threshold_days': 365, 'lock_unused_accounts_enabled': False},
                        'must_one_time_password_enabled': False,
                        'password_expiration_days': 60,
                        'password_expiration_maximum_days_before_lock': 1000,
                        'password_expiration_warning_days': 7}
        password_history: {'check_history_enabled': True, 'repeated_history_length': 10}
        password_strength: {'complexity': 2, 'minimum_length': 6, 'palindrome_check_enabled': True}
"""


RETURN = """
password_policy:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call, checkpoint_argument_spec_for_all


def main():
    # arguments for the module:
    fields = dict(
        lock_settings=dict(
            type='dict',
            options=dict(
                inactivity_settings=dict(
                    type='dict',
                    options=dict(
                        lock_unused_accounts_enabled=dict(type='bool', default=False),
                        inactivity_threshold_days=dict(type='int', default=365)
                    )
                ),
                failed_attempts_settings=dict(
                    type='dict',
                    options=dict(
                        failed_lock_duration_seconds=dict(type='int', default=1200),
                        failed_lock_enforced_on_admin=dict(type='bool', default=False),
                        failed_lock_enabled=dict(type='bool', default=False),
                        failed_attempts_allowed=dict(type='int', default=10)
                    )
                ),
                password_expiration_days=dict(type='raw', no_log=True),
                password_expiration_warning_days=dict(type='int', default=7, no_log=True),
                password_expiration_maximum_days_before_lock=dict(type='raw', no_log=True),
                must_one_time_password_enabled=dict(type='bool', default=False)
            )
        ),
        password_history=dict(
            type='dict',
            options=dict(
                check_history_enabled=dict(type='bool', default=False),
                repeated_history_length=dict(type='int', default=10)
            ),
            no_log=True
        ),
        password_strength=dict(
            type='dict',
            options=dict(
                minimum_length=dict(type='int', default=6),
                complexity=dict(type='int', default=2),
                palindrome_check_enabled=dict(type='bool', default=True)
            ),
            no_log=True
        )
    )

    fields.update(checkpoint_argument_spec_for_all)
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    # handle password_expiration_days, it can get never in addition to integer
    password_expiration_days = module.params.get('password_expiration_days')
    try:
        if password_expiration_days is not None:
            password_expiration_days = int(password_expiration_days)
    except ValueError:
        if password_expiration_days == "never":
            pass
        else:
            module.fail_json(msg="The 'password_expiration_days' parameter must be an integer or never.")

    # handle password_expiration_maximum_days_before_lock, it can get never in addition to integer
    password_expiration_maximum_days_before_lock = module.params.get('password_expiration_maximum_days_before_lock')
    try:
        if password_expiration_maximum_days_before_lock is not None:
            password_expiration_maximum_days_before_lock = int(password_expiration_maximum_days_before_lock)
    except ValueError:
        if password_expiration_maximum_days_before_lock == "never":
            pass
        else:
            module.fail_json(msg="The 'password_expiration_maximum_days_before_lock' parameter must be an integer or never.")

    api_call_object = 'password-policy'

    res = chkp_api_call(module, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
