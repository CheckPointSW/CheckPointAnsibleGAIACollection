.. _cp_gaia_snmp_facts_module:


cp_gaia_snmp_facts -- Show snmp agent configuration.
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show snmp agent configuration.



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

    
    - name: Show SNMP status
      check_point.gaia.cp_gaia_snmp_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

