.. _cp_gaia_ssh_server_settings_facts_module:


cp_gaia_ssh_server_settings_facts -- Show SSH server settings.
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show SSH server settings, request only supported on GAIA versions R81.20+.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  include_disabled_values (False, bool, False)
    Include disabled algorithms.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show SSH server settings
      check_point.gaia.cp_gaia_ssh_server_settings_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  enabled_ciphers (always., list, )
    Enabled ssh ciphers.


  enabled_mac_algorithms (always., list, )
    Enabled ssh mac algorithms.


  enabled_kex_algorithms (always., list, )
    Enabled ssh kex algorithms.


  enabled_public_key_algorithms (Gaia API v1.9 and Gaia R82 and above., list, )
    Enabled ssh public key algorithms.


  password_authentication (Gaia API v1.9 and above., bool, )
    Password authentication status.


  permit_root_login (Gaia API v1.9 and above., bool, )
    Permit root login status.


  use_dns (Gaia API v1.9 and above., bool, )
    Use DNS status.


  client_alive_interval (Gaia API v1.9 and above., int, )
    Client alive interval in seconds.


  login_grace_time (Gaia API v1.9 and Gaia R82 and above., int, )
    Login grace time in seconds.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

