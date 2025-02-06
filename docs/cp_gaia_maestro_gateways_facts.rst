.. _cp_gaia_maestro_gateways_facts_module:


cp_gaia_maestro_gateways_facts -- Show Gateway/s.
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show information regarding Maestro Gateways, either assigned to Security Groups or unassigned.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  id (False, str, None)
    ID (serial number) of Maestro Gateway to show. If not specified, all gateways information is returned.


  include_pending_changes (False, bool, None)
    If true, show pending topology. If false, show deployed topology


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show Maestro Gateways
      check_point.gaia.cp_gaia_gateways_facts:

    - name: Show Maestro Gateway by specifying it's ID
      check_point.gaia.cp_gaia_gateways_facts:
        id: 1007RT1992



Return Values
-------------

ansible_facts (always., dict, )
  The Maestro Gateway/s facts.


  gateways (always, list, )
    List of Maestro Gateways.


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







Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

