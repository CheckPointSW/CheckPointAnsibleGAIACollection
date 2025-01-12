.. _cp_gaia_allowed_clients_module:


cp_gaia_allowed_clients -- Modify the configuration of allowed clients.
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify the configuration of allowed clients.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  allowed_networks (False, list, None)
    Configure allowed clients as network.


    subnet (False, str, None)
      The network subnet.


    mask_length (False, int, None)
      The network mask length.



  allowed_hosts (False, list, None)
    Configure allowed clients as hosts, valid valuse are IPv4/Ipv6 addresses.


  allowed_any_host (False, bool, None)
    Allowed all hosts.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set allowed clients
      check_point.gaia.cp_gaia_allowed_clients:
        allowed_networks: [{"subnet": "44.4.44.0", "mask_length": 24}, {"subnet": "55.4.55.0", "mask_length": 24}]



Return Values
-------------

allowed_clients (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

