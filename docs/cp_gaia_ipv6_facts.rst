.. _cp_gaia_ipv6_facts_module:


cp_gaia_ipv6_facts -- Check IPv6 support in the machine's operating system.
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Check IPv6 support in the machine's operating system.



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

    
    - name: Show IPv6 status
      check_point.gaia.cp_gaia_ipv6_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  enabled (always, bool, )
    Ipv6 enabled (true/false).


  reboot_required (always, bool, )
    Notifying when reboot is required in order for the changes to take effect (Refer to 'run-reboot' API).






Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

