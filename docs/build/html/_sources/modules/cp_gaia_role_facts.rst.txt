.. _cp_gaia_role_facts_module:


cp_gaia_role_facts -- Show role/s information.
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show role information.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    Role name to show. If not specified, all roles information is returned.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show roles
      check_point.gaia.cp_gaia_role_facts:

    - name: Show role by specifying it's name
      check_point.gaia.cp_gaia_role_facts:
        name: test_role




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  state (always, str, )
    Ansible state which can be ``present`` or ``absent``.


  name (always, str, )
    Role name.


  features (always, list, )
    Specifies which features will be assigned to the role.


    name (always, str, )
      Feature name. Valid values are feature name as shown in cp_gaia_features_facts or ``all`` to specify all features.


    permission (always, str, )
      Feature permission. Valid values are ``read-write`` ``read-only``.



  extended_commands (always, list, )
    Specifies which extended commands will be assigned to the role. Valid values are extended commands as shown in cp_gaia_extended_commands_facts API output.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

