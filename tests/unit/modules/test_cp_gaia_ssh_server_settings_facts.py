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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_ssh_server_settings_facts

EXPECTED_RESULT = {
    'enabled_ciphers': ['aes128-ctr', 'aes128-gcm@openssh.com', 'aes192-ctr', 'aes256-ctr', 'aes256-gcm@openssh.com', 'chacha20-poly1305@openssh.com'],
    'enabled_kex_algorithms': [
        'curve25519-sha256', 'curve25519-sha256@libssh.org', 'diffie-hellman-group14-sha1', 'diffie-hellman-group14-sha256',
        'diffie-hellman-group16-sha512', 'diffie-hellman-group18-sha512', 'diffie-hellman-group-exchange-sha256', 'ecdh-sha2-nistp256',
        'ecdh-sha2-nistp384', 'ecdh-sha2-nistp521'
    ],
    'enabled_mac_algorithms': [
        'hmac-sha1', 'hmac-sha1-etm@openssh.com', 'hmac-sha2-256', 'hmac-sha2-256-etm@openssh.com', 'hmac-sha2-512',
        'hmac-sha2-512-etm@openssh.com', 'umac-64-etm@openssh.com', 'umac-64@openssh.com', 'umac-128-etm@openssh.com', 'umac-128@openssh.com'
    ]
}

PAYLOAD = {}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_ssh_server_settings_facts.chkp_facts_api_call'
api_call_object = 'ssh-server-settings'


class TestCheckpointSshServerSettingsFacts(object):
    module = cp_gaia_ssh_server_settings_facts

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    @pytest.fixture
    def connection_mock(self, mocker):
        connection_class_mock = mocker.patch('ansible.module_utils.network.checkpoint.checkpoint.Connection')
        return connection_class_mock.return_value

    def test_facts(self, mocker, connection_mock):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{
            "changed": False,
            api_call_object: EXPECTED_RESULT
        }
        ]
        result = self._run_module(PAYLOAD)
        assert not result['changed']
        assert EXPECTED_RESULT.items() == result['ansible_facts'].items()

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
