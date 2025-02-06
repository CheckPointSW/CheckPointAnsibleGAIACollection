.. _cp_gaia_maestro_gateways_module:


cp_gaia_maestro_gateways -- Modify Security Group Members.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Assign, re-assign or un-assign Gateways to Security Groups, and change GW descriptions.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  id (True, str, None)
    The serial of the Gateway you wish to modify


  security_group (False, int, None)
    Choose ID of Security Group to assign this Gateway to


  description (False, str, None)
    Description of this Gateway


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Assign GW to SG and add description
      check_point.gaia.cp_gaia_gateways:
        id: 1007RT1992
        security_group: 1
        description: "1007RT1992 GW Description"



Return Values
-------------

maestro_gateway (always., dict, )
  The updated Maestro Gateway details.





Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

