.. _cp_gaia_snmp_user_facts_module:


cp_gaia_snmp_user_facts -- Show SNMPv3 USM user/s.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the SNMPv3 USM users currently configured.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  name (False, str, None)
    SNMPv3 USM user name to show. If not specified, all users information is returned.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show SNMP users
      check_point.gaia.cp_gaia_snmp_user_facts:

    - name: Show SNMPv3 USM user by specifying it's name
      check_point.gaia.cp_gaia_snmp_user_facts:
        name: snmpuser




Return Values
-------------

ansible_facts (always., dict, )
  The SNMPv3 USM user/s facts.


  objects (always, list, )
    List of SNMP users.


    name (always, str, )
      SNMPv3 USM User name.


    permission (always, str, )
      User permission.


    allowed_virtual_systems (always, str, )
      Configured Virtual Devices allowed for the USM user - vsid range 0-512.


    authentication (always, dict, )
      Authentication details.


      protocol (always, str, )
        Authentication protocol, MD5 and SHA1 are not supported starting from R81.



    privacy (always, dict, )
      Privacy details.


      protocol (always, str, )
        Privacy protocol.



    data_privacy (always, bool, )
      Related to AutoPriv/AutnNoPriv in SecurityLevel in the RFC. True- AutoPriv ,False- AuthNoPriv.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

