.. _cp_gaia_user_facts_module:


cp_gaia_user_facts -- Show user/s.
==================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the users currently configured.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    User name to show. If not specified, all users information is returned.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show users
      check_point.gaia.cp_gaia_user_facts:

    - name: Show user by specifying it's name
      check_point.gaia.cp_gaia_user_facts:
        name: admin




Return Values
-------------

ansible_facts (always., dict, )
  The user/s facts.


  objects (always, list, )
    List of users.


    name (always, str, )
      User name.


    uid (always, int, )
      User UID.


    homedir (always, str, )
      User home directory.


    primary_system_group_id (always, int, )
      User primary system group id.


    secondary_system_groups (always, list, )
      User secondary system groups.


    real_name (always, str, )
      User real name.


    shell (always, str, )
      User shell.


    allow_access_using (always, list, )
      The access-mechanisms available for a user. Valid values CLI, Web-UI, Gaia-API (supported from R81.10). Default [CLI, Web-UI].


    must_change_password (always, bool, )
      Must\_change\_password.


    roles (always, list, )
      User roles.


    locked (always, bool, )
      If the user has been locked out.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

