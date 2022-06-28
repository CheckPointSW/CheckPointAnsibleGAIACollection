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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_bond_interface

EXPECTED_RESULT = {
    'comments': '{bond5 interface}',
    'dhcp': {'enabled': False},
    'down_delay': '200',
    'enabled': True,
    'ipv4_address': 'Not-Configured',
    'ipv4_mask_length': 'Not-Configured',
    'ipv6_address': 'Not-Configured',
    'ipv6_autoconfig': 'Not configured',
    'ipv6_local_link_address': 'Not Configured',
    'ipv6_mask_length': 'Not-Configured',
    'lacp_rate': 'Not configured',
    'members': [],
    'mii_interval': '100',
    'mode': 'xor',
    'mtu': '1500',
    'name': 'bond5',
    'primary': 'Not configured',
    'status': {'duplex': 'N/A', 'link_state': False, 'rx_bytes': '0', 'rx_packets': '0', 'speed': 'N/A', 'tx_bytes': '0', 'tx_packets': '0'},
    'up_delay': '200',
    'xmit_hash_policy': 'layer2'
}

PAYLOAD = {
    "comments": "bond5 interface",
    "name": "bond5",
    "mode": "xor"
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_bond_interface.chkp_api_call'
api_call_object = 'bond-interface'


class TestCheckpointBondInterface(object):
    module = cp_gaia_bond_interface

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
        assert EXPECTED_RESULT.items() == result['bond_interface'].items()

    def test_idempotent(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, False)

    def test_changed(self, mocker, connection_mock):
        self.run_wrapper(mocker, connection_mock, True)

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
