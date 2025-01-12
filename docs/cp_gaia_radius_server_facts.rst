.. _cp_gaia_radius_server_facts_module:


cp_gaia_radius_server_facts -- Show radius servers settings.
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show radius servers settings.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show radius servers settings.
      check_point.gaia.cp_gaia_radius_server_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  super_user_uid (always, str, )
    The UID that will be given to a super user.


  default_shell (always, str, )
    Default shell when login.


  nas_ip (always, str, )
    The NAS IP for the radius client.


  servers (always, list, )
    Radius servers list.


    priority (always, int, )
      Search priority (lower values comes first). Valid values are -999 - 999.


    secret (always, str, )
      Secret string.


    port (always, int, )
      UDP port to contact on the RADIUS server.


    timeout (always, int, )
      Valid values are 1-50.


    address (always, str, )
      Server address.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

