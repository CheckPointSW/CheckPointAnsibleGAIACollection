==============================
Check_Point.gaia Release Notes
==============================

.. contents:: Topics


v8.0.0
======

Release Summary
---------------

This is release 8.0.0 of ``check_point.gaia``, released on 2026-11-11. It updates the collection for Red Hat Ansible Automation Hub certification; the modules and plugins are unchanged. It is a major release because the minimum supported ansible-core version changed. It replaces 7.1.1, which was not published.

Breaking Changes / Porting Guide
--------------------------------

- The collection now requires ansible-core 2.16 or newer (``requires_ansible: '>=2.16.0'``). ansible-core 2.15 is no longer supported by Red Hat Ansible Automation Platform. Users on ansible-core 2.15 must upgrade ansible-core to 2.16 or newer, or keep using version 7.1.0 of the collection. Other users don't need to change anything.

Minor Changes
-------------

- README - add a Support section, installation instructions for Red Hat Ansible Automation Hub, and the supported Python versions (3.10 and newer, also listed under Requirements); remove the outdated "Ansible 2.9+" requirement.
- README - host the Management Proxy diagram in the CheckPointSW repository.
- tests/config.yml - declare the supported Python versions for modules (``python_requires: ">=3.10"``).
- CI - stop running sanity tests on ansible-core 2.15.

Bugfixes
--------

- README - update the Management Proxy instructions to use the ``ansible_checkpoint_mgmt_proxy_enabled`` inventory variable introduced in 7.1.0, instead of the removed ``mgmt_proxy enabled=True`` host.


v7.1.0
======

Release Summary
---------------

This is release 7.1.0 of ``check_point.gaia``, released on 2026-11-02.

Major Changes
-------------

- Check mode (``--check``) is now supported by all modules. Before this release, running a playbook with ``--check`` applied real changes on the machine. Modules now report the change that would be made without making it; read-only operations (``show-`` APIs and ``cp_gaia_simulate_packet``) still run. A diff is also reported outside check mode, so ``--diff`` works on real runs.

Breaking Changes / Porting Guide
--------------------------------

- httpapi - Management Proxy users only: the plugin no longer reads ``/etc/ansible/hosts`` to detect Management Proxy mode, which caused the connection failures in #72 and #76. Replace the ``mgmt_proxy`` host with ``enabled=True`` in ``/etc/ansible/hosts`` with the inventory variable ``ansible_checkpoint_mgmt_proxy_enabled=true``; otherwise the requests are not forwarded to the target gateway and go to the Gaia API of the Management Server itself. Other users don't need to change anything.

Minor Changes
-------------

- cp_gaia_initial_setup - add the ``grub_password`` parameter.
- cp_gaia_ntp - add the ``preferred`` parameter and the ``server`` and ``pool`` server types (Gaia API v1.8 and above).
- cp_gaia_snmp_pre_defined_traps - add the missing ``lowDiskSpace`` trap parameter.
- cp_gaia_ssh_server_settings - add the ``enabled_public_key_algorithms``, ``password_authentication``, ``permit_root_login``, ``use_dns``, ``client_alive_interval`` and ``login_grace_time`` parameters (Gaia API v1.9 and above).
- cp_gaia_banner - document the API limits of the banner message (80 characters per line, 20 lines).
- galaxy.yml - add ``ansible.netcommon`` as a dependency of the collection.
- Add the GPL-3.0 ``LICENSE`` file, matching the module headers and ``galaxy.yml``.

New Modules
-----------

- check_point.gaia.cp_gaia_param – set Config Point parameters over Web Services API.
- check_point.gaia.cp_gaia_param_facts – get Config Point parameters over Web Services API.

Bugfixes
--------

- httpapi - fix the connection failing on Python 3.12 and newer ansible-core, and in AAP/AWX, because the plugin loaded the local inventory file.
- module_utils - fix task error reporting: read the correct ``error`` field of a failed task, fail when a succeeded task returns a non-zero ``return-value``, and show a readable message instead of a raw response (with a version hint for 404 errors).
- module_utils - show the error message returned in the ``errors`` field of a failed task instead of a generic message.
- module_utils - fix the idempotency check of lists (order-independent) and of values returned with a different type (for example ``4`` and ``"4"``).
- cp_gaia_run_script - fail and report the script's error when the script returns a non-zero exit code, instead of reporting success.
- cp_gaia_ntp - fix idempotency always reporting ``changed=true``, including on Gaia API versions below v1.8.
- cp_gaia_snmp - fix idempotency of ``contact`` and ``location`` when they contain characters the API returns escaped (``:`` and ``\``).
- cp_gaia_simulate_packet, cp_gaia_virtual_systems_facts, cp_gaia_vsnext_state_facts - fix the documented return values to match what the modules return.


v7.0.0
======

Release Summary
---------------

This is release 7.0.0 of ``check_point.gaia``, released on 2025-02-07.

New Modules
-----------

- check_point.gaia.cp_gaia_maestro_changes – apply or discard pending Maestro changes over Web Services API.
- check_point.gaia.cp_gaia_maestro_gateways – manage Maestro Gateways over Web Services API.
- check_point.gaia.cp_gaia_maestro_gateways_facts – get information about Maestro Gateways over Web Services API.
- check_point.gaia.cp_gaia_maestro_ports – configure Maestro Orchestrator ports over Web Services API.
- check_point.gaia.cp_gaia_maestro_ports_facts - get information about Maestro Orchestrator ports over Web Services API.
- check_point.gaia.cp_gaia_maestro_security_groups - manage Maestro Security Groups over Web Services API.
- check_point.gaia.cp_gaia_maestro_security_groups_facts - get information about Maestro Security Groups over Web Services API.
- check_point.gaia.cp_gaia_maestro_sites - add description to Maestro Sites over Web Services API.
- check_point.gaia.cp_gaia_maestro_sites_facts - get information about Maestro Sites over Web Services API.

Minor Changes
---------------

modify infrastructure to support special Maestro APIs.


v6.0.3
======

Release Summary
---------------

this release 6.0.3 of ``check_point.gaia``, released on 2025-02-06.

Bugfixes
---------------

Fix shebang files, modules should not be executable.


v6.0.2
======

Release Summary
---------------

this release 6.0.2 of ``check_point.gaia``, released on 2025-02-06.

Bugfixes
---------------

Fix test lint and issues in uploading the package.


v6.0.1
======

Release Summary
---------------

this release 6.0.1 of ``check_point.gaia``, released on 2025-1-27.

Minor Changes
---------------

Added wait_for_task for the VSNext modules cp_gaia_virtual_switch and cp_gaia_virtual_gateway.

Bugfixes
---------------

Fix the documentation that wasn't loaded in the previous version.


v6.0.0
======

Release Summary
---------------

this release 6.0.0 of ``check_point.gaia``, released on 2025-1-22.

New Modules
-----------

- check_point.gaia.cp_gaia_alias_interface – Manage Alias interface of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_alias_interface_facts – Get information about alias interfaces of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_system_group – Manage system groups of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_system_group_facts – Get information about system groups of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dynamic_content – install policy on a dynamic layer Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dynamic_content_layer_facts – get the details of the installed policy on a given dynamic layer on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_dynamic_content_layers_facts – get the details of all dynamic layers on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_simulate_packet – simulate packet rulebase execution on a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_systems_facts – get virtual-system objects facts on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_switch – manages virtual switch on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_switch_facts – get virtual-switch objects facts on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_gateway – manages virtual-gateway objects on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_gateway_facts – get virtual-gateway objects facts on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_virtual_vsnext_state_facts – get the VSNext state on Check Point VSNext machine over Web Services API.
- check_point.gaia.cp_gaia_grub_password – manage grub password of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_grub_password_facts – get grub hash password of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp –  manage SNMP configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_facts –  get SNMP configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_custom_trap –  manage SNMP custom trap configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_custom_trap_facts –  get SNMP custom trap configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_pre_defined_traps –  manage SNMP pre defined traps configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_pre_defined_traps_facts –  get SNMP pre defined traps configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_trap_receiver –  manage SNMP trap receiver configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_trap_receiver_facts –  get SNMP trap receiver configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_user –  manage SNMP USM user configuration of a Check Point machine over Web Services API.
- check_point.gaia.cp_gaia_snmp_user_facts –  get SNMP USM user configuration of a Check Point machine over Web Services API.

Major Changes
---------------

- Update physical interfaces to Show/Configure dhcp as part of the request.

Bugfixes
---------------

- Fix Password expiration lifetime and Password expiration lockout in password policy to accept never as string in addition to integers values.
- Fix bug: Cannot change password hash of user admin.


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
