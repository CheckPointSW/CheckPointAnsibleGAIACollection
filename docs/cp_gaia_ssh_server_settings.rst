.. _cp_gaia_ssh_server_settings_module:


cp_gaia_ssh_server_settings -- Modify ssh server settings.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify ssh server settings.



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


  enabled_ciphers (False, list, None)
    Enabled ssh ciphers.


  enabled_mac_algorithms (False, list, None)
    Enabled ssh mac algorithms.


  enabled_kex_algorithms (False, list, None)
    Enabled ssh kex algorithms.


  enabled_public_key_algorithms (False, list, None)
    Enabled ssh public key algorithms. Supported from Gaia API v1.9 and Gaia R82.


  password_authentication (False, bool, None)
    Enables or disables password authentication. Supported from Gaia API v1.9.


  permit_root_login (False, bool, None)
    Enables or disables root login. Supported from Gaia API v1.9.


  use_dns (False, bool, None)
    Enables or disables reverse DNS lookup of the client. Supported from Gaia API v1.9.


  client_alive_interval (False, int, None)
    Interval in seconds for sending alive messages to the client, valid values 0-65535. Supported from Gaia API v1.9.


  login_grace_time (False, int, None)
    Time in seconds allowed for a user to log in, valid values 0-240. Supported from Gaia API v1.9 and Gaia R82.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set ssh server settings
      check_point.gaia.cp_gaia_ssh_server_settings:
        enabled_ciphers: ['aes128-ctr', 'aes128-gcm@openssh.com', 'aes192-ctr', 'aes256-ctr',
                          'aes256-gcm@openssh.com', 'chacha20-poly1305@openssh.com']
        enabled_kex_algorithms: ['curve25519-sha256', 'curve25519-sha256@libssh.org',
                                 'diffie-hellman-group14-sha1', 'diffie-hellman-group14-sha256',
                                 'diffie-hellman-group16-sha512', 'diffie-hellman-group18-sha512',
                                 'diffie-hellman-group-exchange-sha256', 'ecdh-sha2-nistp256',
                                 'ecdh-sha2-nistp384', 'ecdh-sha2-nistp521']
        enabled_mac_algorithms: ['hmac-sha1', 'hmac-sha1-etm@openssh.com',
                                 'hmac-sha2-256', 'hmac-sha2-256-etm@openssh.com',
                                 'hmac-sha2-512', 'hmac-sha2-512-etm@openssh.com',
                                 'umac-64-etm@openssh.com', 'umac-64@openssh.com',
                                 'umac-128-etm@openssh.com', 'umac-128@openssh.com']

    - name: Set ssh server access settings
      check_point.gaia.cp_gaia_ssh_server_settings:
        version: '1.9'
        password_authentication: true
        permit_root_login: false
        use_dns: false
        client_alive_interval: 0
        login_grace_time: 120



Return Values
-------------

ssh_server_settings (always., dict, )
  The updated ssh server settings details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

