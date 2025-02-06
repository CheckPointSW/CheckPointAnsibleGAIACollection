.. _cp_gaia_maestro_security_groups_module:


cp_gaia_maestro_security_groups -- Add, modify or delete Secruity Groups.
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add, modify or delete Secruity Groups.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be :literal:`present` or :literal:`absent`.


  id (False, int, None)
    Security Group ID. If not specified, all other fields are required (except description ans sites) as a new SG will be created.


  interfaces (False, list, None)
    Orchestrator ports that will be assigned to this Security Group. At least one of 'id' or 'interface-name' parameters must be provided.


    id (False, str, None)
      Interface ID (e.g. "1/13/1")


    name (False, str, None)
      Interface name (e.g. "eth1-05")


    description (False, str, None)
      Description of the interface



  gateways (False, list, None)
    Maestro Gateways that will be assigned to this Security Group.


    id (optional, str, None)
      Maestro Gateway ID (serial number)


    description (False, str, None)
      Description of this Maestro Gateway



  sites (False, list, None)
    Security Group Site descriptions. The security group is assigned to 'sites' automatically

    according to gateways associated with the Security Group.


    id (optional, int, None)
      ID of this site


    description (optional, str, None)
      Description of this site



  ftw_configuration (False, dict, None)
    First time wizard configuration for this Security Group


    hostname (optional, str, None)
      Hostname for Security Group


    is_vsx (optional, bool, None)
      Determines if this Security Group is a VSX


    one_time_password (optional, str, None)
      One time password for Secure Internal Communication (SIC)


    admin_password (optional, str, None)
      Admin password for Security Group



  mgmt_connectivity (False, dict, None)
    The IP addresses that will be used to manage this Security Group


    ipv4_address (optional, str, None)
      IPv4 address for Security Group


    ipv4_mask_length (optional, int, None)
      IPv4 mask length for Security Group


    default_gateway (optional, str, None)
      Default Gateway address for Security Group



  description (False, str, None)
    Security Group description


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change GWs of SG1
      check_point.gaia.cp_gaia_security_groups:
        id: 1
        gateways: [{id: 1007RT1992}]

    - name: Create new end-to-end SG
      check_point.gaia.cp_gaia_maestro_security_groups:
        interfaces: [{"name": "eth1-Mgmt1"}]
        gateways: [{"id": "3112ET1966"}]
        ftw_configuration: {"hostname": "New_SG", "is_vsx": false, "one_time_password": "otpotp", "admin_password": "adminpassword"}
        mgmt_connectivity: {"ipv4_address": "1.1.1.1", "ipv4_mask_length": 24, "default_gateway": "1.1.1.4"}



Return Values
-------------

maestro_security_group (always., dict, )
  The updated MSecurity Group details.





Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

