.. _cp_gaia_ntp_facts_module:


cp_gaia_ntp_facts -- Show NTP settings.
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the NTP state, servers(primary and secondary) and the current NTP server.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



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

    
    - name: Show current NTP configuration
      check_point.gaia.cp_gaia_ntp_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  enabled (always, bool, )
    active status.


  servers (always, list, )
    Servers list.


    address (always, str, )
      Ipv4-address or Ipv6-address.


    version (always, int, )
      NTP version.


    type (always, str, )
      NTP type.


    status (always, str, )
      NTP status.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

