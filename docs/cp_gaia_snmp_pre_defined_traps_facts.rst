.. _cp_gaia_snmp_pre_defined_traps_facts_module:


cp_gaia_snmp_pre_defined_traps_facts -- Show pre-defined traps.
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show pre-defined traps.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show SNMP pre-defined traps status
      check_point.gaia.cp_gaia_snmp_pre_defined_traps_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

