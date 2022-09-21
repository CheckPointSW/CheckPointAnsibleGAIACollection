.. _cp_gaia_tacacs_server_facts_module:


cp_gaia_tacacs_server_facts -- Show tacacs servers settings.
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show tacacs servers settings.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show tacacs servers settings.
      check_point.gaia.cp_gaia_tacacs_server_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  super_user_uid (always, str, )
    The UID that will be given to a TACACS+ user.


  enabled (always, bool, )
    TACACS-authentication on or off.


  servers (always, list, )
    TACACS servers list.


    priority (always, int, )
      Search priority (lower values comes first). Valid values are -999 - 999.


    secret (always, str, )
      Secret string.


    timeout (always, int, )
      Valid values are 1-50.


    address (always, str, )
      Server address.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

