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


  virtual_system_id (False, int, None)
    Virtual System ID.


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


    polling_frequency (optional, int, None)
      Polling interval in seconds



  custom_traps_settings (optional, dict, None)
    Custom traps settings.


    clear_trap_interval (optional, int, None)
      Interval in second between clear traps


    clear_trap_amount (optional, int, None)
      Number of clear traps that is sent after custom trap termination



  vsx_settings (optional, dict, None)
    VSX settings.


    enabled (optional, bool, None)
      True if SNMP is in vsx mode


    vs_access (optional, str, None)
      SNMP vs-access type direct/indirect queries on Virtual-Devices

      direct- SNMP direct queries on Virtual-Devices

      indirect- SNMP direct queries via VS0


    sysname (optional, bool, None)
      This command is relevant only for VSX with SNMP VS mode, Where

      False = the sysname OID for all Virtual Devices will return the same result VS0 hostname

      True = VS0 sysname OID returns the VSX hostname and Virtual Device sysname OID returns the Check Point object name of the Virtual Device






Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




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

