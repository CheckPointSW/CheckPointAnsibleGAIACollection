.. _cp_gaia_routes_ospf_facts_module:


cp_gaia_routes_ospf_facts -- Show active OSPF routes.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show active OSPF routes.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  limit (False, int, 50)
    The maximum number of returned results.


  offset (False, int, 0)
    The number of results to initially skip.


  order (False, str, ASC)
    Sorts the routes by either ascending or descending order. Valid values are \ :literal:`ASC`\  \ :literal:`DESC`\ .


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show active OSPF routes
      check_point.gaia.cp_gaia_routes_ospf_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  total (always, int, )
    Total number of routes.


  from (always, int, )
    From which route the query was done.


  to (always, int, )
    To which route the query was done.


  objects (always, list, )
    List of all aggregate routes.


  virtual_systems_id (always, int, )
    Virtual System ID.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

