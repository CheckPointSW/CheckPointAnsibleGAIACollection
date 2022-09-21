.. _cp_gaia_tacacs_server_module:


cp_gaia_tacacs_server -- Set TACACS servers settings.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set TACACS servers settings.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  super_user_uid (False, str, None)
    The UID that will be given to a TACACS+ user.


  enabled (False, bool, None)
    TACACS-authentication on or off.


  servers (False, list, None)
    TACACS servers list.


    priority (False, int, None)
      Search priority (lower values comes first). Valid values are -999 - 999.


    secret (False, str, None)
      Secret string.


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

    
    - name: Change TACACS server settings
      check_point.gaia.cp_gaia_tacacs_server:
        enabled: False
        servers: [{"priority": 3, "address": "1.2.1.2", "port": 56, "timeout": 1, "secret": "12345"}]



Return Values
-------------

tacacs (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

