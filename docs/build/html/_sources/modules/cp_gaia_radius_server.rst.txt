.. _cp_gaia_radius_server_module:


cp_gaia_radius_server -- Set radius servers settings.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set radius servers settings.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  super_user_uid (False, str, None)
    The UID that will be given to a super user.


  default_shell (False, str, None)
    Default shell when login.


  nas_ip (False, str, None)
    The NAS IP for the radius client.


  servers (False, list, None)
    Radius servers list.


    priority (False, int, None)
      Search priority (lower values comes first). Valid values are -999 - 999.


    secret (False, str, None)
      Secret string.


    port (False, int, None)
      UDP port to contact on the RADIUS server.


    timeout (False, int, None)
      Valid values are 1-50.


    address (False, str, None)
      Server address.






Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change Radius server settings
      check_point.gaia.cp_gaia_radius_server:
        default_shell: cli
        servers: [{"priority": 3, "address": "1.2.1.2", "port": 56, "timeout": 1, "secret": "12345"}]



Return Values
-------------

radius (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

