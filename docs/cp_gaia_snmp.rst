.. _cp_gaia_snmp_module:


cp_gaia_snmp -- SNMP agent configuration.
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SNMP agent configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  enabled (False, bool, None)
    Enables/Disables the SNMP Agent.


  ver (False, str, None)
    Configures the supported SNMP version v1, v2 and v3.


  trap_usm (False, str, None)
    The user which will generate the SNMP traps, should be existed usm user


  contact (False, str, None)
    SNMP contact string


  location (False, str, None)
    SNMP location string Specifies a string that contains the location for the device.


  read_only_community (False, str, None)
    SNMP read-only community password, Where read-only lets you only read the values of SNMP objects


  read_write_community (False, str, None)
    SNMP read-write community password, Where read-write read and set the values as well


  interfaces (False, str, None)
    Adds a local interface to the list of local interfaces, on which the SNMP daemon listens


  pre_defined_traps_settings (optional, dict, None)
    Pre-defined traps settings.


  custom_traps_settings (optional, dict, None)
    Custom traps settings.


  vsx_settings (optional, dict, None)
    VSX settings.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set SNMP status
      check_point.gaia.cp_gaia_snmp:
        enabled: true




Return Values
-------------

snmp (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

