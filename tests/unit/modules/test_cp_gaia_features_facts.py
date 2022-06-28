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
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_features_facts

EXPECTED_RESULT = {
    'features': [
        {'description': 'Manage interfaces names', 'name': 'interface-name'},
        {'description': 'Run firewall commands from clish', 'name': 'firewall_management'},
        {'description': 'Control CoreXL and Multi Queue', 'name': 'perf'},
        {'description': 'TACACS+ Grants additional permissions to TACACS+ users', 'name': 'tacacs_enable'},
        {'description': 'Control system logging configuration', 'name': 'syslog'},
        {'description': 'Crash Data', 'name': 'core-dump'},
        {'description': 'Manage Gaia Portal configuration', 'name': 'web'},
        {'description': 'Control session parameters, such as inactivity timeout', 'name': 'inactto'},
        {'description': 'Configure authentication through external TACACS/RADIUS servers', 'name': 'aaa-servers'},
        {'description': 'Monitor Security Acceleration Module for information on usage and connections.', 'name': 'sam'},
        {'description': 'Hardware sensor monitoring', 'name': 'sysenv'},
        {'description': 'Hardware asset summary', 'name': 'asset'},
        {
            'description': 'Create a supernet network from the combination of networks with a common routing prefix (supports IPv4 and IPv6)',
            'name': 'aggregate'
        },
        {'description': 'Configure proxy settings', 'name': 'proxy'},
        {'description': 'Configure how the system displays time, date and netmask', 'name': 'format'},
        {'description': 'Configure static ARP entries and proxy ARP entries, control dynamic ARP entries', 'name': 'arp'},
        {'description': 'Configure dynamic routing via the Border Gateway Protocol', 'name': 'bgp'},
        {'description': 'Relays DHCP and BOOTP messages between clients and servers on different IP Network', 'name': 'bootp'},
        {'description': 'System configuration', 'name': 'sysconfig'},
        {'description': 'Scratchpad Configuration', 'name': 'scratchpad'},
        {'description': 'Set the time and date of the system', 'name': 'clock-date'},
        {'description': 'Create backup of the system for events of data loss', 'name': 'backup'},
        {'description': 'Create 2 backup of the system for events of data loss', 'name': 'scheduled_backup'},
        {'description': 'Configure SSH client', 'name': 'ssh-client'},
        {'description': 'Factory Defaults', 'name': 'fcd'},
        {'description': 'Upgrade', 'name': 'upgrade'},
        {'description': 'Schedule automated tasks that perform actions at a specific time', 'name': 'cron'},
        {'description': 'Enable or disable IPv6 stack on this system', 'name': 'ipv6-state'},
        {'description': 'Neighbour Discovery Protocol is used to determine the addresses of other IPv6 nodes', 'name': 'neighbor'},
        {'description': 'Mail notifications will be sent using this email address', 'name': 'ssmtp'},
        {'description': 'Enabling or Disabling the virtualized mode (CLI only)', 'name': 'vsx'},
        {'description': 'Controlling virtual systems (CLI only)', 'name': 'virtual-system'},
        {'description': 'Overview of the system', 'name': 'defaultRO'},
        {'description': 'Default RW Feature', 'name': 'defaultRW'},
        {'description': 'System configurations', 'name': 'system'},
        {'description': 'Firewall configurations', 'name': 'security-gateway'},
        {'description': 'Acceleration data', 'name': 'securexl'},
        {'description': 'Logged users history', 'name': 'file'},
        {'description': 'Logged users history', 'name': 'users-access-log'},
        {'description': 'dynamic-balancing configurations', 'name': 'dynamic-balancing'},
        {'description': 'Spike Detective', 'name': 'spike-detective'},
        {'description': 'Central Deployment Tool', 'name': 'cdt'},
        {'description': 'The ability to define additional extended commands in the CLI', 'name': 'command'},
        {'description': 'Configure Link Layer Discovery Protocol servers', 'name': 'lldp'},
        {'description': "Shows the system's version", 'name': 'version'},
        {'description': 'Configure messages displayed when logging into the system', 'name': 'message'},
        {'description': 'Display blades summary', 'name': 'blades'},
        {'description': 'Automate client network parameter assignment, such as IP address and name servers', 'name': 'dhcp'},
        {'description': 'Configure host name, DNS servers and known hosts', 'name': 'dns'},
        {'description': "Control the system's distribution mode", 'name': 'distribution'},
        {'description': "Control the system's chassis", 'name': 'chassis'},
        {'description': "Control the system's SSM", 'name': 'ssm'},
        {'description': "Control the system's SMO", 'name': 'smo'},
        {'description': 'Control Maestro GW commands', 'name': 'maestro'},
        {'description': 'Advertisement of routing information from one protocol to another (supports IPv4 and IPv6)', 'name': 'export'},
        {'description': 'Configure Inbound Route Filters for RIP, OSPFv2, BGP, and OSPFv3 (supports IPv4 and IPv6)', 'name': 'import'},
        {'description': 'Configure Inbound Route Filters for RIP, OSPFv2, BGP, and OSPFv3 (supports IPv4 and IPv6)', 'name': 'import6'},
        {'description': 'Configure Operating System user groups, for advanced management of file privileges', 'name': 'group'},
        {'description': 'Configure known hosts and their addresses', 'name': 'host'},
        {'description': "Configure the system's name", 'name': 'hostname'},
        {'description': "Set the system's domain name", 'name': 'domainname'},
        {'description': 'Security Groups configuration', 'name': 'SecurityGroups'},
        {'description': 'Shut down the system', 'name': 'reboot_halt'},
        {'description': 'Control the front panel LCD display available on some appliances', 'name': 'lcd'},
        {'description': 'Control which interface is used for management', 'name': 'management_interface'},
        {'description': 'Lights Out Management (LOM) Configuration', 'name': 'lom'},
        {'description': 'Establish multicast group memberships via the Internet Group Management Protocol', 'name': 'igmp'},
        {'description': "Shows a CLI script containing the system's configuration", 'name': 'configuration'},
        {'description': 'Configure interfaces, aliases, bridges and VLANs', 'name': 'interface'},
        {'description': 'IP Conflicts Monitoring', 'name': 'ip-conflicts-monitor'},
        {'description': 'Enables forwarding of UDP broadcast traffic to other interfaces', 'name': 'iphelper'},
        {'description': 'Detects Reachability of IP Addresses', 'name': 'ipreachdetect'},
        {'description': 'Configure IPsec Security Associations for routing protocols.', 'name': 'ipsec-routing'},
        {'description': 'Control how routed interacts with ClusterXL', 'name': 'routed-cluster'},
        {'description': 'Routing Event Trigger', 'name': 'routing-event-trigger'},
        {'description': 'Download SmartConsole', 'name': 'smart-console'},
        {'description': 'Snapshot Scheduled', 'name': 'snapshot_scheduled'},
        {'description': 'Snapshot Management allows creating full backups of the system', 'name': 'snapshot'},
        {'description': "Control Network Time Protocol for synchronizing the system's clock over a network", 'name': 'ntp'},
        {'description': 'Configure dynamic routing via the Intermediate System to Intermediate System protocol', 'name': 'isis'},
        {'description': 'Configure dynamic routing via the Open Shortest-Path First protocol', 'name': 'ospf'},
        {'description': 'Configure IPv6 dynamic routing via the Open Shortest-Path First v3 protocol', 'name': 'ospf3'},
        {'description': 'Configure Protocol-Independent Multicast', 'name': 'pim'},
        {'description': 'Directly Configure Multicast Forwarding Cache', 'name': 'mfc-static'},
        {'description': 'Roles are sets of permissions assigned to users', 'name': 'rba'},
        {'description': 'Configure router discovery', 'name': 'rdisc'},
        {'description': 'Configure dynamic routing via the Routing Information Protocol', 'name': 'rip'},
        {'description': 'Configure dynamic routing via the Routing Information Protocol', 'name': 'ripng'},
        {'description': 'Show route', 'name': 'route'},
        {'description': 'Configure protocol ranks and trace options.', 'name': 'route-options'},
        {'description': 'Prefix Lists and Prefix Trees', 'name': 'prefix'},
        {'description': 'Route Map', 'name': 'routemap'},
        {'description': 'Change your user account password', 'name': 'selfpasswd'},
        {'description': 'Access to the system shell, providing full access', 'name': 'expert'},
        {'description': 'Change The Expert authentication method', 'name': 'expert-authentication-method'},
        {'description': 'Change The Expert Password', 'name': 'expert-password'},
        {'description': 'Change The Expert Password Hash', 'name': 'expert-password-hash'},
        {'description': 'Configure which hosts are allowed to connect to this device.', 'name': 'host-access'},
        {'description': 'Manage License', 'name': 'license'},
        {'description': 'Activate Licenses', 'name': 'license_activation'},
        {'description': 'Manage Certificate Authority', 'name': 'certificate_authority'},
        {'description': 'Monitor your system through the Simple Network Management Protocol', 'name': 'snmp'},
        {'description': 'Configure static routes', 'name': 'static-route'},
        {'description': 'Configure static routes for IPv6 networks', 'name': 'static6'},
        {'description': 'Static Multicast Routes', 'name': 'static-mroute'},
        {'description': 'Configure NAT pool prefixes (supports IPv4 and IPv6)', 'name': 'nat-pool'},
        {'description': 'Configure router discovery', 'name': 'ipv6rdisc6'},
        {'description': 'Configure DHCPv6 Relay', 'name': 'dhcp6relay'},
        {'description': 'View summary information about routes on your system.', 'name': 'show-route-all'},
        {'description': 'Configure policy based routing priority rules and action tables.', 'name': 'pbr-combine-static'},
        {'description': 'Configure user accounts', 'name': 'user'},
        {'description': 'Configure password and account policies', 'name': 'password-controls'},
        {'description': 'Configure NetFlow to export data', 'name': 'netflow'},
        {'description': 'Configure the Virtual Router Redundancy Protocol', 'name': 'vrrp'},
        {'description': 'Configure the Virtual Router Redundancy Protocol, advanced dialog', 'name': 'adv-vrrp'},
        {'description': 'Configure the IPv6 Virtual Router Redundancy Protocol', 'name': 'vrrp6'},
        {'description': 'Hardware sensor monitoring', 'name': 'hw-monitor'},
        {'description': 'RAID volumes monitoring', 'name': 'raid-monitor'},
        {'description': 'Configure High Availability and Load Sharing between a group of systems', 'name': 'cluster_ha'},
        {'description': 'Security Management GUI Clients', 'name': 'mgmt-gui-clients'},
        {'description': 'Appliance Maintenance', 'name': 'prod-maintain'},
        {'description': 'Location Led', 'name': 'location-led'},
        {'description': 'First Time Wizard', 'name': 'ftw'},
        {'description': 'VPN Tunneling', 'name': 'vpnt'},
        {'description': 'Cloning Group', 'name': 'CloningGroup'},
        {'description': 'Cloning Group Management', 'name': 'CloningGroupManagement'},
        {'description': 'Configure Network Access', 'name': 'netaccess'},
        {'description': 'Configure the route-inject mechanism.', 'name': 'route-injection'},
        {'description': 'Consent Flags', 'name': 'consent-flags'},
        {'description': 'Display the update packages status and manage package downloads and installations', 'name': 'installer'},
        {'description': 'Manage deployment policy and mail notifications for software updates', 'name': 'installer_conf'},
        {'description': 'Management Data Plane Separation', 'name': 'mdps'},
        {'description': 'ssl', 'name': 'ssl'},
        {'description': 'Change The Grub2 Password', 'name': 'grub2-password'},
        {'description': 'Change The Grub2 Password Hash', 'name': 'grub2-password-hash'},
        {'description': 'Apply FTW settings using cloud configuration', 'name': 'cloud-config'},
        {'description': 'Inspect aaa feature using REST API', 'name': 'expert_api_aaa'},
        {'description': 'Inspect allowed-clients feature using REST API', 'name': 'expert_api_allowed-clients'},
        {'description': 'Inspect cphaprob feature using REST API', 'name': 'expert_api_cphaprob'},
        {'description': 'Inspect Cluster feature using REST API', 'name': 'expert_api_Cluster'},
        {'description': 'Inspect ioc-feeder feature using REST API', 'name': 'expert_api_ioc-feeder'},
        {'description': 'Inspect routes feature using REST API', 'name': 'expert_api_routes'},
        {'description': 'Inspect syslog feature using REST API', 'name': 'expert_api_syslog'},
        {'description': 'Inspect snmp feature using REST API', 'name': 'expert_api_snmp'},
        {'description': 'Inspect dhcp-server feature using REST API', 'name': 'expert_api_dhcp-server'},
        {'description': 'Inspect dns feature using REST API', 'name': 'expert_api_dns'},
        {'description': 'Inspect files feature using REST API', 'name': 'expert_api_files'},
        {'description': 'Inspect ftw feature using REST API', 'name': 'expert_api_ftw'},
        {'description': 'Inspect groups feature using REST API', 'name': 'expert_api_groups'},
        {'description': 'Inspect hostname feature using REST API', 'name': 'expert_api_hostname'},
        {'description': 'Inspect interface feature using REST API', 'name': 'expert_api_interface'},
        {'description': 'Inspect Interfaces feature using REST API', 'name': 'expert_api_Interfaces'},
        {'description': 'Inspect ipv6 feature using REST API', 'name': 'expert_api_ipv6'},
        {'description': 'Inspect license feature using REST API', 'name': 'expert_api_license'},
        {'description': 'Inspect NTP feature using REST API', 'name': 'expert_api_NTP'},
        {'description': 'Inspect passwordcontrols feature using REST API', 'name': 'expert_api_passwordcontrols'},
        {'description': 'Inspect proxy feature using REST API', 'name': 'expert_api_proxy'},
        {'description': 'Inspect system feature using REST API', 'name': 'expert_api_system'},
        {'description': 'Inspect runScript feature using REST API', 'name': 'expert_api_runScript'},
        {'description': 'Inspect route feature using REST API', 'name': 'expert_api_route'},
        {'description': 'Inspect backup feature using REST API', 'name': 'expert_api_backup'},
        {'description': 'Inspect snapshot feature using REST API', 'name': 'expert_api_snapshot'},
        {'description': 'Inspect Messages feature using REST API', 'name': 'expert_api_Messages'},
        {'description': 'Inspect Misc feature using REST API', 'name': 'expert_api_Misc'},
        {'description': 'Inspect server-status feature using REST API', 'name': 'expert_api_server-status'},
        {'description': 'Inspect asset feature using REST API', 'name': 'expert_api_asset'},
        {'description': 'Inspect diagnostics feature using REST API', 'name': 'expert_api_diagnostics'},
        {'description': 'Inspect users feature using REST API', 'name': 'expert_api_users'},
        {'description': 'Inspect versions feature using REST API', 'name': 'expert_api_versions'},
        {'description': 'Inspect rba-roles feature using REST API', 'name': 'expert_api_rba-roles'},
        {'description': 'Inspect bootp feature using REST API', 'name': 'expert_api_bootp'},
        {'description': 'Inspect ssh-server feature using REST API', 'name': 'expert_api_ssh-server'},
        {'description': 'Inspect cron feature using REST API', 'name': 'expert_api_cron'},
        {'description': 'Inspect features feature using REST API', 'name': 'expert_api_features'},
        {'description': 'Inspect extended-commands feature using REST API', 'name': 'expert_api_extended-commands'},
        {'description': 'Inspect isis feature using REST API', 'name': 'expert_api_isis'},
        {'description': 'Inspect ospf feature using REST API', 'name': 'expert_api_ospf'},
        {'description': 'Inspect grubPassword feature using REST API', 'name': 'expert_api_grubPassword'},
        {'description': 'Inspect expertPassword feature using REST API', 'name': 'expert_api_expertPassword'}
    ]
}

PAYLOAD = {}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_features_facts.chkp_facts_api_call'
api_call_object = 'features'


class TestCheckpointFeaturesFacts(object):
    module = cp_gaia_features_facts

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
