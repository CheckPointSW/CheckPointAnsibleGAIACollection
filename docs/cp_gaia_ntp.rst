.. _cp_gaia_ntp_module:


cp_gaia_ntp -- Sets NTP status and servers.
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Sets NTP status and servers.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  enabled (False, bool, None)
    NTP active status.


  servers (False, list, None)
    Servers to set. Note there cannot be more than one primary/secondary servers.


    version (False, int, None)
      NTP server version. Valid values are 1-4.


    type (False, str, None)
      Server type.


    address (False, str, None)
      Server address (IPv4/IPv6).






Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Setting ntp servers for the system
      check_point.gaia.cp_gaia_ntp:
        enabled: False
        servers: [{"version": 1, "type": "primary", "address": "1.1.1.1"}]



Return Values
-------------

ntp (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

