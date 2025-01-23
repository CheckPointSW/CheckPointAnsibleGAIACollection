.. _cp_gaia_snmp_pre_defined_traps_module:


cp_gaia_snmp_pre_defined_traps -- SNMP agent configuration.
===========================================================

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


  authorizationError (False, dict, None)
    authorizationError Trap.


    enabled (False, bool, None)
      Enables/Disables the authorizationError Trap.



  biosFailure (False, dict, None)
    biosFailure Trap.


    enabled (False, bool, None)
      Enables/Disables the biosFailure Trap.



  configurationChange (False, dict, None)
    configurationChange Trap.


    enabled (False, bool, None)
      Enables/Disables the configurationChange Trap.



  configurationSave (False, dict, None)
    configurationSave Trap.


    enabled (False, bool, None)
      Enables/Disables the configurationSave Trap.



  fanFailure (False, dict, None)
    fanFailure Trap.


    enabled (False, bool, None)
      Enables/Disables the fanFailure Trap.



  highVoltage (False, dict, None)
    highVoltage Trap.


    enabled (False, bool, None)
      Enables/Disables the highVoltage Trap.



  linkUpLinkDown (False, dict, None)
    linkUpLinkDown Trap.


    enabled (False, bool, None)
      Enables/Disables the linkUpLinkDown Trap.



  clusterXLFailover (False, dict, None)
    clusterXLFailover Trap.


    enabled (False, bool, None)
      Enables/Disables the clusterXLFailover Trap.



  lowVoltage (False, dict, None)
    lowVoltage Trap.


    enabled (False, bool, None)
      Enables/Disables the lowVoltage Trap.



  overTemperature (False, dict, None)
    overTemperature Trap.


    enabled (False, bool, None)
      Enables/Disables the overTemperature Trap.



  powerSupplyFailure (False, dict, None)
    powerSupplyFailure Trap.


    enabled (False, bool, None)
      Enables/Disables the powerSupplyFailure Trap.



  raidVolumeState (False, dict, None)
    raidVolumeState Trap.


    enabled (False, bool, None)
      Enables/Disables the raidVolumeState Trap.



  vrrpv2AuthFailure (False, dict, None)
    vrrpv2AuthFailure Trap.


    enabled (False, bool, None)
      Enables/Disables the vrrpv2AuthFailure Trap.



  vrrpv2NewMaster (False, dict, None)
    vrrpv2NewMaster Trap.


    enabled (False, bool, None)
      Enables/Disables the vrrpv2NewMaster Trap.



  vrrpv3NewMaster (False, dict, None)
    vrrpv3NewMaster Trap.


    enabled (False, bool, None)
      Enables/Disables the vrrpv3NewMaster Trap.



  vrrpv3ProtoError (False, dict, None)
    vrrpv3ProtoError Trap.


    enabled (False, bool, None)
      Enables/Disables the vrrpv3ProtoError Trap.



  coldStart (False, dict, None)
    coldStart Trap.


    enabled (False, bool, None)
      Enables/Disables the coldStart Trap.


    threshold (False, int, None)
      coldStart threshold (seconds), prevents sending coldStart trap when system up-time is greater than the threshold


    reboot_only (False, bool, None)
      ColdStart reboot only, allows sending ColdStart trap only on reboot



  lowDiskSpaceAllPartitions (False, dict, None)
    lowDiskSpaceAllPartitions Trap.


    enabled (False, bool, None)
      Enables/Disables the lowDiskSpaceAllPartitions Trap.






Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set SNMP pre_defined traps
      check_point.gaia.cp_gaia_snmp_pre_defined_traps:
        biosFailure: {enabled: true}




Return Values
-------------

snmp_pre_defined_traps (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

