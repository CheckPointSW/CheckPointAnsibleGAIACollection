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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_physical_interfaces_facts

EXPECTED_RESULT_ALL = {
    "objects": [
        {
            "auto-negotiation": True,
            "comments": "",
            "duplex": "Not-Configured",
            "enabled": True,
            "ipv4-address": "172.23.21.136",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:9e:a8:2c",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "Not-Configured",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "4015323875",
                "rx-packets": "3484339",
                "speed": "1000M",
                "tx-bytes": "58977236",
                "tx-packets": "370140"
            },
            "tx-ringsize": "1024"
        },
        {
            "auto-negotiation": "Not configured",
            "comments": "",
            "duplex": "Not-Configured",
            "enabled": False,
            "ipv4-address": "Not-Configured",
            "ipv4-mask-length": "Not-Configured",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:9e:dd:09",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth1",
            "rx-ringsize": "256",
            "speed": "Not-Configured",
            "status": {
                "duplex": "full",
                "link-state": False,
                "rx-bytes": "0",
                "rx-packets": "0",
                "speed": "1000M",
                "tx-bytes": "0",
                "tx-packets": "0"
            },
            "tx-ringsize": "1024"
        }
    ]
}

EXPECTED_RESULT_SINGLE = {
        "auto-negotiation": True,
        "comments": "",
        "duplex": "Not-Configured",
        "enabled": True,
        "ipv4-address": "172.23.21.136",
        "ipv4-mask-length": "24",
        "ipv6-address": "Not-Configured",
        "ipv6-autoconfig": "Not configured",
        "ipv6-local-link-address": "Not Configured",
        "ipv6-mask-length": "Not-Configured",
        "mac-addr": "00:50:56:9e:a8:2c",
        "monitor-mode": "Not configured",
        "mtu": "1500",
        "name": "eth0",
        "rx-ringsize": "256",
        "speed": "Not-Configured",
        "status": {
            "duplex": "full",
            "link-state": True,
            "rx-bytes": "4015337823",
            "rx-packets": "3484429",
            "speed": "1000M",
            "tx-bytes": "58981342",
            "tx-packets": "370170"
        },
        "tx-ringsize": "1024"
    }

PAYLOAD = {
    "name": "eth0"
}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_physical_interfaces_facts.api_call'


class TestCheckpointPhysicalInterfacesFacts(object):
    module = cp_gaia_physical_interfaces_facts

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    @pytest.fixture
    def connection_mock(self, mocker):
        connection_class_mock = mocker.patch('ansible.module_utils.network.checkpoint.checkpoint.Connection')
        return connection_class_mock.return_value

    def test_show_all(self, mocker, connection_mock):
        api_call_response = {
            "objects": [
                {
                    "auto-negotiation": True,
                    "comments": "",
                    "duplex": "Not-Configured",
                    "enabled": True,
                    "ipv4-address": "172.23.21.136",
                    "ipv4-mask-length": "24",
                    "ipv6-address": "Not-Configured",
                    "ipv6-autoconfig": "Not configured",
                    "ipv6-local-link-address": "Not Configured",
                    "ipv6-mask-length": "Not-Configured",
                    "mac-addr": "00:50:56:9e:a8:2c",
                    "monitor-mode": "Not configured",
                    "mtu": "1500",
                    "name": "eth0",
                    "rx-ringsize": "256",
                    "speed": "Not-Configured",
                    "status": {
                        "duplex": "full",
                        "link-state": True,
                        "rx-bytes": "4015323875",
                        "rx-packets": "3484339",
                        "speed": "1000M",
                        "tx-bytes": "58977236",
                        "tx-packets": "370140"
                    },
                    "tx-ringsize": "1024"
                },
                {
                    "auto-negotiation": "Not configured",
                    "comments": "",
                    "duplex": "Not-Configured",
                    "enabled": False,
                    "ipv4-address": "Not-Configured",
                    "ipv4-mask-length": "Not-Configured",
                    "ipv6-address": "Not-Configured",
                    "ipv6-autoconfig": "Not configured",
                    "ipv6-local-link-address": "Not Configured",
                    "ipv6-mask-length": "Not-Configured",
                    "mac-addr": "00:50:56:9e:dd:09",
                    "monitor-mode": "Not configured",
                    "mtu": "1500",
                    "name": "eth1",
                    "rx-ringsize": "256",
                    "speed": "Not-Configured",
                    "status": {
                        "duplex": "full",
                        "link-state": False,
                        "rx-bytes": "0",
                        "rx-packets": "0",
                        "speed": "1000M",
                        "tx-bytes": "0",
                        "tx-packets": "0"
                    },
                    "tx-ringsize": "1024"
                }
            ]
        }

        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [api_call_response]
        result = self._run_module(PAYLOAD)
        assert not result['changed']
        assert EXPECTED_RESULT_ALL.items() == result['ansible_facts'].items()


    def test_show_single(self, mocker, connection_mock):
        api_call_response = {
            "auto-negotiation": True,
            "comments": "",
            "duplex": "Not-Configured",
            "enabled": True,
            "ipv4-address": "172.23.21.136",
            "ipv4-mask-length": "24",
            "ipv6-address": "Not-Configured",
            "ipv6-autoconfig": "Not configured",
            "ipv6-local-link-address": "Not Configured",
            "ipv6-mask-length": "Not-Configured",
            "mac-addr": "00:50:56:9e:a8:2c",
            "monitor-mode": "Not configured",
            "mtu": "1500",
            "name": "eth0",
            "rx-ringsize": "256",
            "speed": "Not-Configured",
            "status": {
                "duplex": "full",
                "link-state": True,
                "rx-bytes": "4015337823",
                "rx-packets": "3484429",
                "speed": "1000M",
                "tx-bytes": "58981342",
                "tx-packets": "370170"
            },
            "tx-ringsize": "1024"
        }

        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [api_call_response]
        result = self._run_module(PAYLOAD)
        assert not result['changed']
        assert EXPECTED_RESULT_SINGLE.items() == result['ansible_facts'].items()


    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
