.. _cp_gaia_virtual_systems_facts_module:


cp_gaia_virtual_systems_facts -- Show Virtual Systems.
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show Virtual Systems.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.8.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show Virtual Systems
      check_point.gaia.cp_gaia_virtual_systems_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The Virtual Systems facts.


  objects (always, list, )
    List of configured Virtual Systems.


    id (always, int, )
      Virtual System ID.


    name (always, str, )
      Virtual System name.


    virtual_system_type (always, str, )
      Virtual System type, Gateway or Switch.


    interfaces (always, list, )
      Network interfaces attached to the Virtual System.



  from (always, int, )
    From which element number the query was done.


  to (always, int, )
    To which element number the query was done.


  total (always, int, )
    Total number of elements returned by the query.






Status
------





Authors
~~~~~~~

- Omer Hadad (@chkp-omerhad)

