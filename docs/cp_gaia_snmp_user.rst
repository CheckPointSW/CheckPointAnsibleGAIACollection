.. _cp_gaia_snmp_user_module:


cp_gaia_snmp_user -- Change a SNMPv3 USM user's characteristics.
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change a SNMPv3 USM user's characteristics.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  state (False, str, present)
    Ansible state which can be :literal:`present` or :literal:`absent`.


  name (True, str, None)
    SNMPv3 USM user name.


  permission (optional, str, None)
    User permission.


  allowed_virtual_systems (optional, str, None)
    Configured Virtual Devices allowed for the USM user - vsid range 0-512.


  authentication (optional, dict, None)
    Authentication details.


    protocol (optional, str, None)
      Authentication protocol, MD5 and SHA1 are not supported starting from R81.


    password (optional, str, None)
      Authentication Password - (8 or more printable characters, Limited by 128 characters)

      Each SNMPv3 USM user must have an authentication pass phrase.


    password_hash (optional, str, None)
      Authentication Hashed Password - (8 or more printable characters, Limited by 128 characters)

      Each SNMPv3 USM user must have an authentication pass phrase.



  privacy (optional, dict, None)
    Privacy details.


    protocol (optional, str, None)
      Privacy protocol.


    password (optional, str, None)
      Privacy Password - (8 or more printable characters, Limited by 128 characters)

      An SNMPv3 USM user with a privacy security level must have a privacy pass phrase.


    password_hash (optional, str, None)
      Privacy Hashed Password - (8 or more printable characters, Limited by 128 characters)

      An SNMPv3 USM user with a privacy security level must have a privacy pass phrase.






Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set permission field for the snmp user
      check_point.gaia.cp_snmp_gaia_user:
        permission: read-only
        name: snmpuser



Return Values
-------------

snmp_user (always., dict, )
  The updated user details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

