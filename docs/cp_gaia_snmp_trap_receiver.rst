.. _cp_gaia_snmp_trap_receiver_module:


cp_gaia_snmp_trap_receiver -- Change the SNMP trap receiver configuration.
==========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change the SNMP trap receiver configuration.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  state (False, str, present)
    Ansible state which can be :literal:`present` or :literal:`absent`.


  address (True, str, None)
    Receiver address.


  ver (optional, str, None)
    Receiver version.


  community_string (optional, str, None)
    Receiver community - Required only in case of v1/v2 versions

    Trap Community String used by the trap receiver to determine which traps are accepted from a device.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set community string for SNMP trap receiver
      check_point.gaia.cp_gaia_snmp_trap_receiver:
        community_string: some_string
        address: trap_receiver_address



Return Values
-------------

snmp_trap_receiver (always., dict, )
  The updated trap receiver details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

