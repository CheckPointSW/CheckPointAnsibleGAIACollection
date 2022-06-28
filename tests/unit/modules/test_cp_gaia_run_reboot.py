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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_run_reboot

EXPECTED_RESULT = {
    'tasks': [
        {
            'execution-time': '98.47',
            'last-update-time': '2022-06-15T11:52+3.00.0',
            'progress-description': 'Reboot done',
            'progress-percentage': 100,
            'start-time': '2022-06-15T11:51+3.00.0',
            'status': 'succeeded',
            'status-code': 200,
            'task-details': [],
            'task-id': 'e0107117-8804-4649-b87e-5c32780f9d2c',
            'task-name': '/run-reboot',
            'time-spent-in-queue': '0.09'
        }
    ]
}

PAYLOAD = {}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_run_reboot.chkp_api_operation'
api_call_object = 'run-reboot'


class TestCheckpointRunReboot(object):
    module = cp_gaia_run_reboot

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
        assert EXPECTED_RESULT.items() == result['run_reboot'].items()

    def test_idempotent(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, False)

    def test_changed(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, True)

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
