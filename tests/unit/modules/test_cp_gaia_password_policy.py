#!/usr/bin/env python
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

from __future__ import absolute_import, division, print_function
__metaclass__ = type
import pytest
from units.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
from ansible.module_utils import basic
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_password_policy

EXPECTED_RESULT = {
    'lock_settings': {
        'failed_attempts_settings': {
            'failed_attempts_allowed': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
            'failed_lock_duration_seconds': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
            'failed_lock_enabled': False, 'failed_lock_enforced_on_admin': False
        },
        'inactivity_settings': {'inactivity_threshold_days': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'lock_unused_accounts_enabled': False},
        'must_one_time_password_enabled': False,
        'password_expiration_days': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
        'password_expiration_maximum_days_before_lock': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
        'password_expiration_warning_days': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    },
    'password_history': {
        'check_history_enabled': True,
        'repeated_history_length': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    },
    'password_strength': {
        'complexity': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
        'minimum_length': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
        'palindrome_check_enabled': True
    }
}

PAYLOAD = {
    'lock_settings': {
        'failed_attempts_settings': {
            'failed_attempts_allowed': 10,
            'failed_lock_duration_seconds': 1200,
            'failed_lock_enabled': False,
            'failed_lock_enforced_on_admin': False
        },
        'inactivity_settings': {'inactivity_threshold_days': 365, 'lock_unused_accounts_enabled': False},
        'must_one_time_password_enabled': False,
        'password_expiration_days': 60,
        'password_expiration_maximum_days_before_lock': 1000,
        'password_expiration_warning_days': 7
    },
    'password_history': {'check_history_enabled': True, 'repeated_history_length': 10},
    'password_strength': {'complexity': 2, 'minimum_length': 6, 'palindrome_check_enabled': True}
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_password_policy.chkp_api_call'
api_call_object = 'password-policy'


class TestCheckpointPasswordPolicy(object):
    module = cp_gaia_password_policy

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    @pytest.fixture
    def connection_mock(self, mocker):
        connection_class_mock = mocker.patch('ansible.module_utils.network.checkpoint.checkpoint.Connection')
        return connection_class_mock.return_value

    def run_wrapper(self, mocker, connection_mock, changed):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{
            "changed": changed,
            api_call_object: EXPECTED_RESULT
        }
        ]
        result = self._run_module(PAYLOAD)
        assert result['changed'] == changed
        assert EXPECTED_RESULT.items() == result['password_policy'].items()

    def test_idempotent(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, False)

    def test_changed(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, True)

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
