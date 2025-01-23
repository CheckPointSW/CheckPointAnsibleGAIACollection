.. _cp_gaia_snmp_custom_trap_module:


cp_gaia_snmp_custom_trap -- Change the SNMP custom\_trap configuration.
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change the SNMP custom\_trap configuration.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (True, str, None)
    Custom trap name.


  oid (optional, str, None)
    OID (object identifier).


  operator (optional, str, None)
    Comparison operator.


  threshold (optional, raw, None)
    The value you want to compare to.


  frequency (optional, int, None)
    Polling interval in seconds.


  msg (optional, str, None)
    Custom trap message.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set threshold for custom trap
      check_point.gaia.cp_gaia_snmp_custom_trap:
        threshold: 12
        name: custom_trap_name




Return Values
-------------

snmp_custom_trap (always., dict, )
  The updated custom trap details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

