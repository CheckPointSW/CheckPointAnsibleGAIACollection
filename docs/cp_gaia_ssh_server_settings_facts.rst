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


  include_disabled_values (False, bool, False)
    Include disabled algorithms.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




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






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

