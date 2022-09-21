.. _cp_gaia_static_route_facts_module:


cp_gaia_static_route_facts -- Show the configuration of static route.
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the configuration of static route.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  limit (False, int, 50)
    The maximum number of returned results. relevant in case facts for all routes.


  offset (False, int, 0)
    The number of results to initially skip. relevant in case facts for all routes.


  order (False, str, ASC)
    Sorts the routes by either ascending or descending order. Valid values are ``ASC`` ``DESC``. relevant in case facts for all routes.


  address (False, str, None)
    Existing IPv4 address, required in case fact for single route.


  mask_length (False, int, None)
    Existing mask length address.Valid values are 0-32, required in case fact for single route.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show active static routes
      check_point.gaia.cp_gaia_static_route_facts:



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






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

