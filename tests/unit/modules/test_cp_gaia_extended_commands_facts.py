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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_extended_commands_facts

EXPECTED_RESULT = {
    'extended_commands': [
        {'description': 'SmartLSM command line', 'name': 'LSMcli', 'path': '/bin/LSMcli_start'},
        {'description': 'Enable SmartLSM', 'name': 'LSMenabler', 'path': '/bin/LSMenabler_start'},
        {'description': 'IPS Snort conversion tool', 'name': 'SnortConvertor', 'path': '/bin/cpSnortConvertor_start'},
        {'description': 'Start, stop, or check status of API server', 'name': 'api', 'path': '/bin/api_wrap'},
        {'description': 'Check Point system configuration utility', 'name': 'cp_conf', 'path': '/bin/cp_conf_start'},
        {'description': 'Run Check Point Internal CA', 'name': 'cpca', 'path': '/bin/cpca_start'},
        {'description': 'Manage/configure Check Point Internal CA', 'name': 'cpca_client', 'path': '/bin/cpca_client_start'},
        {'description': 'Create new Check Point Internal CA database', 'name': 'cpca_create', 'path': '/bin/cpca_create_start'},
        {'description': 'Print/convert Check Point Internal CA database', 'name': 'cpca_dbutil', 'path': '/bin/cpca_dbutil_start'},
        {'description': 'Check Point software configuration utility', 'name': 'cpconfig', 'path': '/bin/cpconfig_start'},
        {'description': 'Clustering commands', 'name': 'cphaprob', 'path': '/bin/cphaprob_start'},
        {'description': 'Enables the High Availability feature on the machine', 'name': 'cphastart', 'path': '/bin/cphastart_start'},
        {'description': 'Disables the High Availability feature on the machine', 'name': 'cphastop', 'path': '/bin/cphastop_start'},
        {'description': 'Show Check Point diagnostics information', 'name': 'cpinfo', 'path': '/opt/CPinfo-10/bin/cpinfo'},
        {'description': 'Add/Remove Check Point licenses', 'name': 'cplic', 'path': '/bin/cplic_start'},
        {'description': 'Show SVN Foundation version', 'name': 'cpshared_ver', 'path': '$CPDIR/bin/cpshared_ver'},
        {'description': 'Start Check Point products installed', 'name': 'cpstart', 'path': '/bin/cpstart_start'},
        {'description': 'Show Check Point statistics info', 'name': 'cpstat', 'path': '/bin/cpstat_start'},
        {'description': 'Stop Check Point products installed', 'name': 'cpstop', 'path': '/bin/cpstop_start'},
        {'description': 'Show Check Point and system online statistics info', 'name': 'cpview', 'path': '/bin/cpview_start'},
        {'description': 'Check Point watchdog administration tool', 'name': 'cpwd_admin', 'path': '/bin/cpwd_admin_start'},
        {'description': 'Send system diagnostics information', 'name': 'diag', 'path': '/bin/cpdiag_send'},
        {'description': 'Endpoint Policy Server commands', 'name': 'dtps', 'path': '/bin/dtps_start'},
        {'description': 'Starts QoS', 'name': 'etmstart', 'path': '/bin/etmstart_start'},
        {'description': 'Stops QoS', 'name': 'etmstop', 'path': '/bin/etmstop_start'},
        {'description': 'QoS commands', 'name': 'fgate', 'path': '/bin/fgate_start'},
        {'description': 'Turns on/off FIPS mode', 'name': 'fips', 'path': '/bin/fips'},
        {'description': 'Security Gateway commands', 'name': 'fw', 'path': '/bin/cpfw_start'},
        {'description': 'SecureXL commands', 'name': 'fwaccel', 'path': '/bin/fwaccel_start'},
        {'description': 'Security Management commands', 'name': 'fwm', 'path': '/bin/fwm_start'},
        {'description': 'Deprecated. Use show interface or set interface instead', 'name': 'ifconfig', 'path': '/etc/deprecated_ifconfig'},
        {'description': 'IPS management commands', 'name': 'ips', 'path': '/bin/cpips_start'},
        {'description': 'Setting LOM IP address', 'name': 'lomipset', 'path': '/bin/lomipset'},
        {'description': 'Print network connections, routing tables and interface statistics', 'name': 'netstat', 'path': '/bin/netstat'},
        {'description': 'Ping a host', 'name': 'ping', 'path': '/bin/ping'},
        {'description': 'Ping a host using IPv6', 'name': 'ping6', 'path': '/bin/ping6'},
        {'description': 'RAID Monitoring tool', 'name': 'raid_diagnostic', 'path': '/bin/raid_diagnostic'},
        {'description': 'RAID Configuration and Monitoring tool', 'name': 'raidconfig', 'path': '/sbin/raidconfig'},
        {'description': 'Monitoring blade commands', 'name': 'rtm', 'path': '/bin/rtm_start'},
        {'description': 'Start Monitoring blade', 'name': 'rtmstart', 'path': '/bin/rtmstart_start'},
        {'description': 'Stop Monitoring blade', 'name': 'rtmstop', 'path': '/bin/rtmstop_start'},
        {'description': 'Monitor top services', 'name': 'rtmtopsvc', 'path': '/bin/rtmtopsvc_start'},
        {'description': 'SecureXL Implementation Module commands', 'name': 'sim', 'path': '/bin/sim_start'},
        {'description': 'Threat Emulation Blade shell', 'name': 'tecli', 'path': '/bin/tecli_start'},
        {'description': 'Show the most active system processes', 'name': 'top', 'path': '/bin/top_start'},
        {'description': 'Trace the route to a host', 'name': 'traceroute', 'path': '/bin/traceroute'},
        {'description': 'Control VPN', 'name': 'vpn', 'path': '/bin/vpn_start'},
        {'description': 'Control VSX gateways', 'name': 'vsx_util', 'path': '/bin/vsx_util_start'}
    ]
}

PAYLOAD = {}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_extended_commands_facts.chkp_facts_api_call'
api_call_object = 'extended-commands'


class TestCheckpointExtendedCommandsFacts(object):
    module = cp_gaia_extended_commands_facts

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
