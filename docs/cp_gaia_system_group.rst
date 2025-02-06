.. _cp_gaia_system_group_module:


cp_gaia_system_group -- Change system group configuration.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change system group configuration.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  state (False, str, present)
    Ansible state which can be :literal:`present` or :literal:`absent`.


  name (True, str, None)
    System group name.


  gid (False, int, None)
    Specifies a numeric group ID used to identify the group, duplicate GIDs are not allowed.


  users (False, list, None)
    List of users in the group.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add new system group
      check_point.gaia.cp_gaia_system_group:
        name: new_group
        members:
          - admin



Return Values
-------------

group (always., dict, )
  The updated group details.





Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

