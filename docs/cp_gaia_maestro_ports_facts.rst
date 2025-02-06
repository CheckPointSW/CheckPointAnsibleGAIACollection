.. _cp_gaia_maestro_ports_facts_module:


cp_gaia_maestro_ports_facts -- Show port/s.
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show information regarding Maestro Orchestrator ports.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  id (False, str, None)
    ID port to show (e.g. '1/13/1'). If both id and interface\_name are not specified, all ports information is returned.


  interface_name (False, str, None)
    Interface name in case this port is an Uplink or MGMT interface (e.g. 'eth1-25').

    If both id and interface\_name are not specified, all ports information is returned.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show Orchestrator ports
      check_point.gaia.cp_gaia_user_facts:

    - name: Show Orchestrator port by specifying it's ID
      check_point.gaia.cp_gaia_user_facts:
        id: 1/13/1



Return Values
-------------

ansible_facts (always., dict, )
  The Maestro port/s facts.


  ports (always, list, )
    List of Maestro ports.


    id (always, str, )
      Port ID.


    site (always, int, )
      Site this Port belongs to.


    interface_name (always, str, )
      Interface name, in case this Port is of Uplink or Management type.


    type (always, str, )
      Port type, either Uplink, Downlink, Site Sync, SSM Sync or Mgmt.


    qsfp_mode (always, str, )
      Port QSFO Mode.


    enabled (always, bool, )
      Indicates whether this port is enabled by the user. AKA 'admin state'.


    link_state (always, bool, )
      True if this Port link is up, false otherwise.


    auto_negotiation (always, bool, )
      True if Auto Negotiation is up for this port, false otherwise.


    transceiver_state (always, str, )
      can be one of PLUGGED/UNPLUGGED.


    operating_speed (always, int, )
      Operating speed of this port.


    mtu (always, int, )
      MTU of this port.


    rx_frames (always, int, )
      Amount of received frames of this port.


    tx_frames (always, int, )
      Amount of transmitted frames of this port.


    orchestrator_id (always, list, )
      Security Group ID(s) in case this port is assigned to a security-group(s). Otherwise, empty list.







Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

