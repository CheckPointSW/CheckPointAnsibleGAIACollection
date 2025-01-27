.. _cp_gaia_snmp_custom_trap_facts_module:


cp_gaia_snmp_custom_trap_facts -- Show SNMP custom traps.
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the SNMP custom trap currently configured.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  name (False, str, None)
    Custom trap name.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show SNMP custom trap
      check_point.gaia.cp_gaia_snmp_custom_trap_facts:

    - name: Show SNMP custom trap by specifying it's name
      check_point.gaia.cp_gaia_snmp_custom_trap_facts:
        name: custom_trap_name




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

