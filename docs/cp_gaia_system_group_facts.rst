.. _cp_gaia_system_group_facts_module:


cp_gaia_system_group_facts -- Show system group/s.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the system groups currently configured.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  name (False, str, None)
    System group name to show. If not specified, all system groups information is returned.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show system groups
      check_point.gaia.cp_gaia_system_group_facts:
    - name: Show system group by specifying it's name
      check_point.gaia.cp_gaia_system_group_facts:
        name: users



Return Values
-------------

ansible_facts (always., dict, )
  The system group/s facts.


  objects (always, list, )
    List of system groups.


    name (always, str, )
      System group name.


    gid (always, int, )
      System group GID.


    users (always, list, )
      List of group members.







Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

