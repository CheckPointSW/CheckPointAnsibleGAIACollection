# Check Point Ansible Gaia Collection
This Ansible collection provides control over a Check Point machine using
Check Point's web-services APIs.

This is the repository of the gaia collection which can be found here - https://galaxy.ansible.com/check_point/gaia

Installation instructions
-------------------------
Run `ansible-galaxy collection install check_point.gaia`

Requirements
------------
* Ansible 2.9+ is required.
* The Check Point server should have Gaia API engine installed on. More information can be found at [Gaia REST API SK](https://supportcenter.checkpoint.com/supportcenter/portal?action=portlets.SearchResultMainAction&eventSubmit_doGoviewsolutiondetails=&solutionid=sk143612).

Usage
-----
1. Edit the `hosts` so that it will contain a section similar to this one:
```
[check_point]
%CHECK_POINT_MANAGEMENT_SERVER_IP%
[check_point:vars]
ansible_httpapi_use_ssl=True
ansible_httpapi_validate_certs=False
ansible_user=%CHECK_POINT_GAIA_USER%
ansible_password=%CHECK_POINT_GAIA_PASSWORD%
ansible_network_os=check_point.gaia.checkpoint
```
<br><br>2. Run a playbook:
```sh
ansible-playbook your_ansible_playbook.yml
```

Example playbook:
```
---
- name: Playbook name
  hosts: check_point
  connection: httpapi
  tasks:
    - name: task to have network
      check_point.gaia.cp_gaia_hostname:
        name: "newhost"
```
Modules
-------
* `cp_gaia_hostname` – Manage the hostname of a Check Point machine over Web Services API.
* `cp_gaia_hostname_facts` – Get the hostname of a Check Point machine over Web Services API.
* `cp_gaia_physical_interface` – Manage physical interface of a Check Point machine over Web Services API.
* `cp_gaia_physical_interfaces_facts` – Get information about physical interfaces of a Check Point machine over Web Services API.
* `cp_gaia_put_file` – Add a new file to a Check Point machine over Web Services API.
* `cp_gaia_allowed_clients` – manage allowed clients of a Check Point machine over Web Services API.
* `cp_gaia_allowed_clients_facts` – get allowed clients of a Check Point machine over Web Services API.
* `cp_gaia_api_versions_facts` –  get api versions of a Check Point machine over Web Services API.
* `cp_gaia_asset_facts` –  get assets of a Check Point machine over Web Services API.
* `cp_gaia_banner` –  manage banner message of a Check Point machine over Web Services API.
* `cp_gaia_banner_facts` –  get banner message of a Check Point machine over Web Services API.
* `cp_gaia_hostname_on_login_page` –  manage hostname_on_login_page message of a Check Point machine over Web Services API.
* `cp_gaia_hostname_on_login_page_facts` –  get hostname_on_login_page message of a Check Point machine over Web Services API.
* `cp_gaia_message_of_the_day` –  manage message_of_the_day message of a Check Point machine over Web Services API.
* `cp_gaia_message_of_the_day_facts` –  get message_of_the_day message of a Check Point machine over Web Services API.
* `cp_gaia_bond_interface` –  manage bond interface of a Check Point machine over Web Services API.
* `cp_gaia_bond_interface_facts` –  get bond interface of a Check Point machine over Web Services API.
* `cp_gaia_vlan_interface` –  manage vlan interface of a Check Point machine over Web Services API.
* `cp_gaia_vlan_interface_facts` –  get vlan interface of a Check Point machine over Web Services API.
* `cp_gaia_bridge_interface` –  manage bridge interface of a Check Point machine over Web Services API.
* `cp_gaia_bridge_interface_facts` –  get bridge interface of a Check Point machine over Web Services API.
* `cp_gaia_dhcp_server` –  manage dhcp server of a Check Point machine over Web Services API.
* `cp_gaia_dhcp_server_facts` –  get dhcp server of a Check Point machine over Web Services API.
* `cp_gaia_radius_server` –  manage radius server of a Check Point machine over Web Services API.
* `cp_gaia_radius_server_facts` –  get radius server of a Check Point machine over Web Services API.
* `cp_gaia_tacacs_server` –  manage tacacs server of a Check Point machine over Web Services API.
* `cp_gaia_tacacs_server_facts` –  get tacacs server of a Check Point machine over Web Services API.
* `cp_gaia_dns` –  manage dns configuration of a Check Point machine over Web Services API.
* `cp_gaia_dns_facts` –  get dns configuration of a Check Point machine over Web Services API.
* `cp_gaia_ntp` –  manage ntp configuration of a Check Point machine over Web Services API.
* `cp_gaia_ntp_facts` –  get ntp configuration of a Check Point machine over Web Services API.
* `cp_gaia_proxy` –  manage proxy configuration of a Check Point machine over Web Services API.
* `cp_gaia_proxy_facts` –  get proxy configuration of a Check Point machine over Web Services API.
* `cp_gaia_password_policy` –  manage password policy configuration of a Check Point machine over Web Services API.
* `cp_gaia_password_policy_facts` –  get password policy configuration of a Check Point machine over Web Services API.
* `cp_gaia_extended_commands_facts` –  get extended commands of a Check Point machine over Web Services API.
* `cp_gaia_features_facts` –  get features of a Check Point machine over Web Services API.
* `cp_gaia_ipv6` –  manage ipv6 configuration of a Check Point machine over Web Services API.
* `cp_gaia_ipv6_facts` –  get ipv6 configuration of a Check Point machine over Web Services API.
* `cp_gaia_initial_setup` –  manage initial setup (FTW) configuration of a Check Point machine over Web Services API.
* `cp_gaia_run_script` –  run script on a Check Point machine over Web Services API.
* `cp_gaia_run_reboot` –  run reboot on a Check Point machine over Web Services API.
* `cp_gaia_remote_syslog` –  manage remote syslog configuration of a Check Point machine over Web Services API.
* `cp_gaia_remote_syslog_facts` –  get remote syslog configuration of a Check Point machine over Web Services API.
* `cp_gaia_syslog` –  manage syslog configuration of a Check Point machine over Web Services API.
* `cp_gaia_syslog_facts` –  get syslog configuration of a Check Point machine over Web Services API.
* `cp_gaia_role` –  manage roles configuration of a Check Point machine over Web Services API.
* `cp_gaia_role_facts` –  get roles configuration of a Check Point machine over Web Services API.
* `cp_gaia_user` –  manage users configuration of a Check Point machine over Web Services API.
* `cp_gaia_user_facts` –  get users configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_aggregate_facts` –  get routes aggregate configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_bgp_facts` –  get routes bgp configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_direct_facts` –  get routes direct configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_facts` –  get routes configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_kernel_facts` –  get routes kernel configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_ospf_facts` –  get routes ospf configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_rip_facts` –  get routes rip configuration of a Check Point machine over Web Services API.
* `cp_gaia_routes_static_facts` –  get routes static configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_job` –  manage scheduled job configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_job_facts` –  get scheduled job configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_job_mail` –  manage scheduled job mail configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_job_mail_facts` –  get scheduled job mail configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_snapshot` –  manage scheduled snapshot configuration of a Check Point machine over Web Services API.
* `cp_gaia_scheduled_snapshot_facts` –  get scheduled snapshot configuration of a Check Point machine over Web Services API.
* `cp_gaia_diagnostics_facts` –  get diagnostics configuration of a Check Point machine over Web Services API.
* `cp_gaia_diagnostics_topics_facts` –  get diagnostics topics configuration of a Check Point machine over Web Services API.
* `cp_gaia_ssh_server_settings` –  manage ssh server settings of a Check Point machine over Web Services API.
* `cp_gaia_ssh_server_settings_facts` –  get ssh server settings of a Check Point machine over Web Services API.
* `cp_gaia_static_route` –  manage static route configuration of a Check Point machine over Web Services API.
* `cp_gaia_static_route_facts` –  get static route configuration of a Check Point machine over Web Services API.
* `cp_gaia_task_facts` –  show task in a Check Point machine over Web Services API.
* `cp_gaia_timezones_facts` –  show time zones in a Check Point machine over Web Services API.
* `cp_gaia_version_facts` –  show gaia version in a Check Point machine over Web Services API.
* `cp_gaia_expert_password` – manage expert password of a Check Point machine over Web Services API.
* `cp_gaia_expert_password_facts` – get expert hash password of a Check Point machine over Web Services API.
* `cp_gaia_time_and_date` – manage time and date and timezone of a Check Point machine over Web Services API.
* `cp_gaia_time_and_date_facts` – get time and date and timezone of a Check Point machine over Web Services API.
* `cp_gaia_virtual_systems_facts` – get virtual-system objects facts on Check Point over Web Services API.
* `cp_gaia_virtual_switch` – manages virtual switch on Check Point machine over Web Services API.
* `cp_gaia_virtual_switch_facts` – get virtual-switch objects facts on Check machine Point over Web Services API.
* `cp_gaia_virtual_gateway` – manages virtual-gateway objects on Check Point machine over Web Services API.
* `cp_gaia_virtual_gateway_facts` – get virtual-gateway objects facts on Check Point machine over Web Services API.
* `cp_gaia_virtual_vsnext_state_facts` – get the VSNext state on Check Point machine over Web Services API.
* `cp_gaia_dynamic_content` – install policy on a dynamic layer Check Point machine over Web Services API.
* `cp_gaia_dynamic_content_layer_facts` – get the details of the installed policy on a given dynamic layer on a Check Point machine over Web Services API.
* `cp_gaia_dynamic_content_layers_facts` – get the details of all dynamic layers on a Check Point machine over Web Services API.
* `cp_gaia_simulate_packet` – simulate packet rulebase execution on a Check Point machine over Web Services API.
* `cp_gaia_alias_interface` – Manage Alias interface of a Check Point machine over Web Services API.
* `cp_gaia_alias_interface_facts` – Get information about alias interfaces of a Check Point machine over Web Services API.
* `cp_gaia_system_group` – Manage system groups of a Check Point machine over Web Services API.
* `cp_gaia_system_group_facts` – Get information about system groups of a Check Point machine over Web Services API.


### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/CheckPointSW/CheckPointAnsibleGAIACollection/blob/master/CHANGELOG.rst).

## Roadmap

We plan to regularly release minor and patch versions, whenever new features are added or bugs fixed. Our collection follows [semantic versioning](https://semver.org/), so breaking changes will only happen in major releases.

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.


## Supported Python versions

- Modules and plugins require Python 2.7 or newer


# Check Point Ansible Proxy Integration

## Overview

This feature integrating the Proxy API for Check Point Security Gateways through the Management Server. The Proxy API enables the Management Server to forward API requests to designated gateways, eliminating the need to address each gateway individually.


 ![image](https://github.com/nilsujma-dev/Check-Point-Ansible-Proxy-Integration/assets/114651180/0a9dc69f-2a64-4511-bb95-01e28f0049af)



## Integration Process

### Step 1: Options Selected

1. **Source Code:** 

The revised code introduces a significant enhancement – the 'target gateway' option. This addition allows the specification of a designated gateway to receive API requests, leveraging the Management Server's Proxy API feature. This modification expands the module's capabilities, aligning with advanced network management requirements and enabling more precise API interactions.

## How to Use

1. Edit the `hosts` so that it will contain a new section similar to this one:
```
[check_point_mgmt]
mgmt_proxy enabled=True
```
2. in the playbook add this var under each task:
```
vars:
    ansible_checkpoint_target: <target_gatway>
```
3. in `hosts` change ansible_user and ansible_password to management credintials
3. Follow the standard Ansible playbook execution process with the enhanced Check Point Ansible Collection.


