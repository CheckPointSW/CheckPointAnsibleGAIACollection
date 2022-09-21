.. _cp_gaia_ipv6_module:


cp_gaia_ipv6 -- Enables/Disables IPv6 support in the machine's operating system.
================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enables/Disables IPv6 support in the machine's operating system.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  enabled (False, bool, None)
    No Documentation available.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set IPv6 status
      check_point.gaia.cp_gaia_ipv6:
        enabled: true




Return Values
-------------

ipv6 (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

