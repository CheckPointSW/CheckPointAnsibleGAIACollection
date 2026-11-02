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
import copy
import pytest
from units.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson, AnsibleFailJson
from ansible.module_utils import basic
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_param

PARAM_PATH = 'gaia.infra.httpd.cp_httpd_configuration.children_core_dumps'

EXPECTED_RESULT = {
    'tasks': [
        {
            'progress-description': 'succeeded',
            'progress-percentage': 100,
            'status': 'succeeded',
            'status-code': 200,
            'task-details': [
                {
                    'changed-params': 1,
                    'dry-run': False,
                    'matched-params': 1,
                    'param-list': [
                        {
                            'comments': 'enabled for debugging purpose',
                            'current-value': True,
                            'default-value': False,
                            'name': PARAM_PATH,
                            'pending': {'action': 'n/a', 'pending_value': 'n/a'},
                            'value-changed': True,
                            'virtual-system-id': 0
                        }
                    ],
                    'pending-params': 0,
                    'sp-members': 'n/a'
                }
            ],
            'task-name': '/set-param'
        }
    ]
}

PAYLOAD = {
    'param_list': [
        {
            'param_path': PARAM_PATH,
            'value': True,
            'comments': 'enabled for debugging purpose'
        }
    ]
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_param.chkp_api_operation'
api_call_object = 'set-param'


def result_with_changed_params(changed_params):
    result = copy.deepcopy(EXPECTED_RESULT)
    details = result['tasks'][0]['task-details'][0]
    details['changed-params'] = changed_params
    details['param-list'][0]['value-changed'] = changed_params > 0
    return result


class TestCheckpointParam(object):
    module = cp_gaia_param

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    def run_wrapper(self, mocker, changed_params, module_args=None):
        api_result = result_with_changed_params(changed_params)
        mock_function = mocker.patch(function_path)
        # the module computes 'changed' itself, so the operation's value must be ignored
        mock_function.side_effect = [{
            "changed": True,
            api_call_object.replace('-', '_'): api_result
        }]
        result = self._run_module(module_args or PAYLOAD)
        assert result['changed'] == (changed_params > 0)
        assert api_result.items() == result['set_param'].items()
        return mock_function

    def test_idempotent(self, mocker):
        self.run_wrapper(mocker, 0)

    def test_changed(self, mocker):
        self.run_wrapper(mocker, 1)

    def test_check_mode_uses_dry_run(self, mocker):
        args = dict(PAYLOAD, _ansible_check_mode=True)
        mock_function = self.run_wrapper(mocker, 1, args)
        module = mock_function.call_args[0][0]
        assert module.params['dry_run'] is True
        assert mock_function.call_args[1]['read_only'] is True

    def test_virtual_system_id_is_sent_as_string(self, mocker):
        mock_function = self.run_wrapper(mocker, 1, dict(PAYLOAD, virtual_system_id=2))
        # the API rejects a Virtual System ID that is not a string
        assert mock_function.call_args[0][0].params['virtual_system_id'] == '2'

    def test_no_task_details_assumes_changed(self, mocker):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{"changed": True, "set_param": {"task_id": "63c53f94"}}]
        result = self._run_module(dict(PAYLOAD, wait_for_task=False))
        assert result['changed'] is True

    def test_value_and_use_default_are_mutually_exclusive(self, mocker):
        args = {'param_list': [{'param_path': PARAM_PATH, 'value': True, 'use_default': True}]}
        set_module_args(args)
        with pytest.raises(AnsibleFailJson):
            self.module.main()

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
