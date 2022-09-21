.. _cp_gaia_proxy_facts_module:


cp_gaia_proxy_facts -- Show proxy setting.
==========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show proxy setting.






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

    
    - name: Show proxy setting
      check_point.gaia.cp_gaia_proxy_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  address (always, str, )
    Ipv4-address or Ipv6-address.


  port (always, int, )
    Proxy port.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

