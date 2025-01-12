.. _cp_gaia_proxy_module:


cp_gaia_proxy -- Change proxy setting.
======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change proxy setting.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  address (False, str, None)
    IPv4/IPv6 address.


  port (False, int, None)
    Proxy server port.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set new static route
      check_point.gaia.cp_gaia_proxy:
        state: present
        address: 1.2.125.0
        port: 89




Return Values
-------------

proxy (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

