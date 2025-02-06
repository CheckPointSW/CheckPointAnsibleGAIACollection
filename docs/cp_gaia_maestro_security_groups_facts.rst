.. _cp_gaia_maestro_security_groups_facts_module:


cp_gaia_maestro_security_groups_facts -- Show Maestro Security Groups topology.
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show Maestro Security Groups topology.






Parameters
----------

  include_pending_changes (False, bool, None)
    If true, show pending topology, as opposed to the one actually deployed


  id (False, int, None)
    ID of Security Group to show. If not specified, all Security Groups information is returned


  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show current information of Security Group 1
      check_point.gaia.cp_gaia_maestro_security_groups_facts:
          id: 1
          include_pending_changes: false



Return Values
-------------

ansible_facts (always., dict, )
  The Maestro Security Group/s facts.


  security_groups (always, list, )
    List of Security Groups.


    id (always, int, )
      Security Group ID.


    interfaces (always, list, )
      The interfaces that are assigned to the Security Group.


      id (always, str, )
        Port ID.


      interface_name (always, str, )
        Interface name.


      description (always, str, )
        Description of this interface.


      vlans (always, list, )
        VLANs this interface belongs to



    gateways (always, list, )
      The Maestro Gateways that are assigned to the Security Group.


      id (always, str, )
        Maestro Gateway ID.


      site (always, int, )
        Site this Gateway belongs to.


      security_group (always, int, )
        The Security Group this Gateway belongs to.


      member_id (always, int, )
        The member ID of this Gateway, if it's assigned to a Security Group.


      model (always, str, )
        Model of this Gateway.


      version (always, dict, )
        OS version installed on this Gateway.


        major (always, str, )
          Major version



      downlink_ports (always, list, )
        The Orchestrator ports which are connected to the Gateway.


        orchestrator_id (always, str, )
          ID of the Orchestrator to which this port belongs


        port (always, str, )
          Port ID



      description (always, str, )
        Description of this Gateway.


      state (always, str, )
        State of this Gateway.


      weight (always, int, )
        Weight assigned to this Gateway, in case it's assigned to a Security Group.



    sites (always, list, )
      List of site descriptions in this Security Group context


      id (always, int, )
        ID of this site


      description (always, str, )
        Description of this site



    ftw_configuration (always, dict, )
      First time wizard configuration for this Security Group


      hostname (always, str, )
        Hostname of this Security Group


      is_vsx (always, bool, )
        Is this Security Group a VSX


      one_time_password (always, str, )
        One time password of Secure Internal Communication (SIC)


      admin_password (always, str, )
        Admin password od Security Group



    mgmt_connectivity (always, dict, )
      The IP addresses that will be used to manage this Security Group


      ipv4_address (always, str, )
        IPv4 address of this Security Group


      ipv4_mask_length (always, int, )
        IPv4 mask length for Security Group


      default_gateway (always, str, )
        Default Gateway address for Security Group



    description (always, str, )
      Description of this Security Group.







Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

