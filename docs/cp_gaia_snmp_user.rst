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


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (True, str, None)
    SNMPv3 USM user name.


  permission (optional, str, None)
    User permission.


  allowed_virtual_systems (optional, str, None)
    Configured Virtual Devices allowed for the USM user - vsid range


  authentication (optional, dict, None)
    Authentication details.


  privacy (optional, dict, None)
    Privacy details.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




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

