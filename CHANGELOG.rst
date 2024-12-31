==============================
Check_Point.gaia Release Notes
==============================

.. contents:: Topics
    
v6.0.0
======

Release Summary
---------------

This is release 6.0.0 of ``check_point.gaia``, released on 2024-12-31.

New Modules
-----------
cp_gaia_virtual_systems_facts – get virtual-system objects facts on Check Point machine over Web Services API.
cp_gaia_virtual_switch – manages virtual switch on Check Point machine over Web Services API.
cp_gaia_virtual_switch_facts – get virtual-switch objects facts on Check Point machine over Web Services API.
cp_gaia_virtual_gateway – manages virtual-gateway objects on Check Point machine over Web Services API.
cp_gaia_virtual_gateway_facts – get virtual-gateway objects facts on Check Point machine over Web Services API.
cp_gaia_virtual_vsnext_state_facts – get the VSNext state on Check Point machine over Web Services API.

v6.0.0
======

Release Summary
---------------

this release 6.0.0 of ``check_point.gaia``, released on 2023-11-1.

New Modules
-----------

- check_point.gaia.cp_gaia_dynamic_content – install policy on a dynamic layer Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dynamic_content_layer_facts – get the details of the installed policy on a given dynamic layer on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dynamic_content_layers_facts – get the details of all dynamic layers on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_simulate_packet – simulate packet rulebase execution on a Check Point machine over Web Services API.


v5.0.1
======

Release Summary
---------------

this release 5.0.1 of ``check_point.gaia``, released on 2023-10-26.

Minor Changes
---------------

update ansible min supported version to 2.14.0 as the old one is EoL.


v5.0.0
======

Release Summary
---------------

This is release 5.0.0 of ``check_point.gaia``, released on 2023-10-01.

New Modules
-----------

- check_point.gaia.cp_gaia_expert_password – manage expert password of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_expert_password_facts – get expert hash password of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_time_and_date – manage time and date and timezone of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_time_and_date_facts – get time and date and timezone of a Check Point machine over Web Services API.

v4.1.1
======

Bugfixes
---------------

- improve infrastructure for idempotency check.
- fix some modules which didn't work as expected (Scheduled Job, Role, Proxy, physical interface, users, ntp, banner message, static route)

v4.1.0
======

Release Summary
---------------

this release 4.1.0 of ``check_point.gaia``, released on 2022-09-21.

Minor Changes
---------------

add the ability to send gaia_api version within the request.

Bugfixes
---------------

add idempotincy check before each present request. do not send the request if it the same configuration in the machine.

v4.0.0
======

Release Summary
---------------

A new major release of ``check_point.gaia``, released on 2022-08-18.

Major Changes
---------------

- breaking facts modules output and make it use ansible_facts in return value.

v3.0.0
======

Release Summary
---------------

This is release 3.0.0 of ``check_point.gaia``, released on 2022-06-30.

New Modules
-----------

- check_point.gaia.cp_gaia_allowed_clients – manage allowed clients of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_allowed_clients_facts – get allowed clients of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_api_versions_facts –  get api versions of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_asset_facts –  get assets of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_banner –  manage banner message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_banner_facts –  get banner message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_hostname_on_login_page –  manage hostname_on_login_page message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_hostname_on_login_page_facts –  get hostname_on_login_page message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_message_of_the_day –  manage message_of_the_day message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_message_of_the_day_facts –  get message_of_the_day message of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_bond_interface –  manage bond interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_bond_interface_facts –  get bond interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_vlan_interface –  manage vlan interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_vlan_interface_facts –  get vlan interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_bridge_interface –  manage bridge interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_bridge_interface_facts –  get bridge interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dhcp_server –  manage dhcp server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dhcp_server_facts –  get dhcp server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_radius_server –  manage radius server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_radius_server_facts –  get radius server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_tacacs_server –  manage tacacs server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_tacacs_server_facts –  get tacacs server of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ntp –  manage ntp configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ntp_facts –  get ntp configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_proxy –  manage proxy configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_proxy_facts –  get proxy configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_password_policy –  manage password policy configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_password_policy_facts –  get password policy configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_extended_commands_facts –  get extended commands of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_features_facts –  get features of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_initial_setup –  manage initial setup (FTW) configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_run_script –  run script on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_run_reboot –  run reboot on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_role –  manage roles configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_role_facts –  get roles configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_user –  manage users configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_user_facts –  get users configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_aggregate_facts –  get routes aggregate configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_bgp_facts –  get routes bgp configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_direct_facts –  get routes direct configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_facts –  get routes configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_kernel_facts –  get routes kernel configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_ospf_facts –  get routes ospf configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_rip_facts –  get routes rip configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_routes_static_facts –  get routes static configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_job –  manage scheduled job configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_job_facts –  get scheduled job configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_job_mail –  manage scheduled job mail configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_job_mail_facts –  get scheduled job mail configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_snapshot –  manage scheduled snapshot configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_scheduled_snapshot_facts –  get scheduled snapshot configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_diagnostics_facts –  get diagnostics configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_diagnostics_topics_facts –  get diagnostics topics configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ssh_server_settings –  manage ssh server settings of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ssh_server_settings_facts –  get ssh server settings of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_static_route –  manage static route configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_static_route_facts –  get static route configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_task_facts –  show task in a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_timezones_facts –  show time zones in a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_version_facts –  show gaia version in a Check Point machine over Web Services API.

v2.0.0
======

New Modules
-----------

- check_point.gaia.cp_gaia_dns –  manage dns configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dns_facts –  get dns configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ipv6 –  manage ipv6 configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_ipv6_facts –  get ipv6 configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_remote_syslog –  manage remote syslog configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_remote_syslog_facts –  get remote syslog configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_syslog –  manage syslog configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_syslog_facts –  get syslog configuration of a Check Point machine over Web Services API.


v1.0.0
======

New Modules
-----------

- check_point.gaia.cp_gaia_hostname – Manage the hostname of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_hostname_facts – Get the hostname of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_physical_interface – Manage physical interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_physical_interfaces_facts – Get information about physical interfaces of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_put_file – Add a new file to a Check Point machine over Web Services API.
