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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_physical_interface

EXPECTED_RESULT = {
    "auto-negotiation": True,
    "comments": "{eth0 interface}",
    "duplex": "full",
    "enabled": True,
    "ipv4-address": "1.2.3.4",
    "ipv4-mask-length": "24",
    "ipv6-address": "Not-Configured",
    "ipv6-autoconfig": "Not configured",
    "ipv6-local-link-address": "Not Configured",
    "ipv6-mask-length": "Not-Configured",
    "mac-addr": "00:50:56:12:12:12",
    "monitor-mode": "Not configured",
    "mtu": "1500",
    "name": "eth0",
    "rx-ringsize": "256",
    "speed": "1000M",
    "status": {
        "duplex": "full",
        "link-state": True,
        "rx-bytes": "3903699193",
        "rx-packets": "2770047",
        "speed": "1000M",
        "tx-bytes": "101801967",
        "tx-packets": "1341294"
    },
    "tx-ringsize": "1024"
}

NOT_CHANGED_PAYLOAD = {
    "name": "eth0",
    "enabled": True,
    "ipv4_address": "1.2.3.4",
    "ipv4_mask_length": 24
}

CHANGED_PAYLOAD = {
    "name": "eth0",
    "enabled": True,
    "ipv4_address": "1.2.3.4",
    "ipv4_mask_length": 24
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_physical_interface.api_call'
api_call_object = 'physical_interface'


class TestCheckpointPhysicalInterface(object):
    module = cp_gaia_physical_interface

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    @pytest.fixture
    def connection_mock(self, mocker):
        connection_class_mock = mocker.patch('ansible.module_utils.network.checkpoint.checkpoint.Connection')
        return connection_class_mock.return_value

    def test_idempotent(self, mocker, connection_mock):
        show_response = {
            "auto-negotiation": True,
            "comments": "{eth0 interface}",
            "duplex": "full",
            "enabled": True,
            "ipv4-address": "1.2.3.4",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:12:12:12",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "1000M",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "3903699193",
                "rx-packets": "2770047",
                "speed": "1000M",
                "tx-bytes": "101801967",
                "tx-packets": "1341294"
            },
            "tx-ringsize": "1024"
        }
        set_response = {
            "auto-negotiation": True,
            "comments": "{eth0 interface}",
            "duplex": "full",
            "enabled": True,
            "ipv4-address": "1.2.3.4",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:12:12:12",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "1000M",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "3903699193",
                "rx-packets": "2770047",
                "speed": "1000M",
                "tx-bytes": "101801967",
                "tx-packets": "1341294"
            },
            "tx-ringsize": "1024"
        }
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [show_response, set_response]
        result = self._run_module(NOT_CHANGED_PAYLOAD)
        assert not result['changed']
        assert EXPECTED_RESULT.items() == result[api_call_object].items()

    def test_changed(self, mocker, connection_mock):
        show_response = {
            "auto-negotiation": True,
            "comments": "{eth0 interface}",
            "duplex": "full",
            "enabled": True,
            "ipv4-address": "1.2.3.5",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:12:12:12",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "1000M",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "3903699193",
                "rx-packets": "2770047",
                "speed": "1000M",
                "tx-bytes": "101801967",
                "tx-packets": "1341294"
            },
            "tx-ringsize": "1024"
        }
        set_response = {
            "auto-negotiation": True,
            "comments": "{eth0 interface}",
            "duplex": "full",
            "enabled": True,
            "ipv4-address": "1.2.3.4",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:12:12:12",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "1000M",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "3903699193",
                "rx-packets": "2770047",
                "speed": "1000M",
                "tx-bytes": "101801967",
                "tx-packets": "1341294"
            },
            "tx-ringsize": "1024"
        }
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [show_response, set_response]
        result = self._run_module(CHANGED_PAYLOAD)
        assert result['changed']
        assert EXPECTED_RESULT.items() == result[api_call_object].items()

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
