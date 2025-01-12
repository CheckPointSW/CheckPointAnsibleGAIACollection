.. _cp_gaia_role_module:


cp_gaia_role -- Modify role.
============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify role.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (True, str, None)
    Role name.


  features (False, list, None)
    Specifies which features will be assigned to the role.


    name (False, str, None)
      Feature name. Valid values are feature name as shown in cp\_gaia\_features\_facts or \ :literal:`all`\  to specify all features.


    permission (False, str, None)
      Feature permission. Valid values are \ :literal:`read-write`\  \ :literal:`read-only`\ .



  extended_commands (False, list, None)
    Specifies which extended commands will be assigned to the role. Valid values are extended commands as shown in cp\_gaia\_extended\_commands\_facts API output.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add new role
      check_point.gaia.cp_gaia_role:
        name: myrole
        extended_commands: ['LSMenabler']
        features: [{"name": "dhcp", "permission": "read-write"},
                   {"name": "ntp", "permission": "read-write"},
                   {"name": "syslog", "permission": "read-write"},
                   {"name": "backup", "permission": "read-only"}]




Return Values
-------------

role (always., dict, )
  The updated role details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

