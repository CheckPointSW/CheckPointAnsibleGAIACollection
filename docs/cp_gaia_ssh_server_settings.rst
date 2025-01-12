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


  enabled_ciphers (False, list, None)
    Enabled ssh ciphers.


  enabled_mac_algorithms (False, list, None)
    Enabled ssh mac algorithms.


  enabled_kex_algorithms (False, list, None)
    Enabled ssh kex algorithms.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




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



Return Values
-------------

ssh_server_settings (always., dict, )
  The updated ssh server settings details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

