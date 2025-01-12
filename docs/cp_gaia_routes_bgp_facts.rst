.. _cp_gaia_routes_bgp_facts_module:


cp_gaia_routes_bgp_facts -- Show active BGP routes.
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show active BGP routes.



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





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show active BGP routes
      check_point.gaia.cp_gaia_routes_bgp_facts:



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

