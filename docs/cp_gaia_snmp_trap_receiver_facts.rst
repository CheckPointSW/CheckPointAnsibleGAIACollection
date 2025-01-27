.. _cp_gaia_snmp_trap_receiver_facts_module:


cp_gaia_snmp_trap_receiver_facts -- Show snmp trap receivers.
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show snmp trap receivers.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  address (False, str, None)
    Receiver address.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show all SNMP trap receivers
      check_point.gaia.cp_gaia_snmp_trap_receiver_facts:

    - name: Show SNMP trap receiver by specifying it's address
      check_point.gaia.cp_gaia_snmp_trap_receiver_facts:
        address: receiver_address




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

