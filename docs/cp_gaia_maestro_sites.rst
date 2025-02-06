.. _cp_gaia_maestro_sites_module:


cp_gaia_maestro_sites -- Set site description.
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set site description.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  site_id (True, int, None)
    ID of site.


  descriptions (False, list, None)
    Provide optional site description per Security Group.


    security_group (optional, int, None)
      The Site Security Group


    description (optional, str, None)
      Site description



  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set site 1 description
      check_point.gaia.cp_gaia_sites:
        site_id: 1
        descriptions: [{security_group: 1, description: "New Description"}]



Return Values
-------------

maestro_site (always., dict, )
  The updated site details.





Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

