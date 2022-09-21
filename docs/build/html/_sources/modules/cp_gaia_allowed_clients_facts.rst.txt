.. _cp_gaia_allowed_clients_facts_module:


cp_gaia_allowed_clients_facts -- Show the configuration of allowed clients.
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the configuration of allowed clients.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



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

    
    - name: Show allowed clients
      check_point.gaia.cp_gaia_allowed_clients_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  allowed_any_host (always, bool, )
    Allowed any host to access the server.


  allowed_hosts (always, list, )
    Lists of allowed hosts.


  allowed_networks (always, list, )
    List of allowed networks.


    subnet (, str, )
      The network subnet.


    mask_length (, int, )
      The network mask length.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

