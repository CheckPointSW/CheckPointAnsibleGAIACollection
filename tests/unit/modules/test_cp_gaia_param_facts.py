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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_param_facts

EXPECTED_RESULT = {
    'tasks': [
        {
            'progress-description': 'succeeded',
            'progress-percentage': 100,
            'status': 'succeeded',
            'status-code': 200,
            'task-details': [
                {
                    'param-list': [
                        {
                            'comments': 'n/a',
                            'current-value': 30,
                            'default-value': 30,
                            'description': 'Timeout for Gunicorn workers in seconds',
                            'last-modified': 'n/a',
                            'name': 'gaia.infra.rest_api.gunicorn.timeout',
                            'pending': {'action': 'n/a', 'pending_value': 'n/a'},
                            'virtual-system-id': 0
                        }
                    ]
                }
            ],
            'task-name': '/show-param'
        }
    ]
}

PAYLOAD = {
    'param_path': 'gaia.infra.rest_api.gunicorn.timeout'
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_param_facts.chkp_api_operation'
api_call_object = 'show-param'


class TestCheckpointParamFacts(object):
    module = cp_gaia_param_facts

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    def test_show(self, mocker):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{
            "changed": True,
            api_call_object.replace('-', '_'): EXPECTED_RESULT
        }]
        result = self._run_module(PAYLOAD)
        # showing parameters never changes the system
        assert result['changed'] is False
        assert EXPECTED_RESULT.items() == result['show_param'].items()
        assert mock_function.call_args[0][1] == api_call_object

    def test_virtual_system_id_is_sent_as_string(self, mocker):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{"changed": True, "show_param": EXPECTED_RESULT}]
        self._run_module(dict(PAYLOAD, virtual_system_id=2))
        # the API rejects a Virtual System ID that is not a string
        assert mock_function.call_args[0][0].params['virtual_system_id'] == '2'

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
