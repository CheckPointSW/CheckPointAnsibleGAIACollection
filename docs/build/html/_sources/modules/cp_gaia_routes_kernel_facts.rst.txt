.. _cp_gaia_routes_kernel_facts_module:


cp_gaia_routes_kernel_facts -- Show active kernel routes.
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show active kernel routes.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  limit (False, int, 50)
    The maximum number of returned results.


  offset (False, int, 0)
    The number of results to initially skip.


  order (False, str, ASC)
    Sorts the routes by either ascending or descending order. Valid values are ``ASC`` ``DESC``.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show active kernel routes
      check_point.gaia.cp_gaia_routes_kernel_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

