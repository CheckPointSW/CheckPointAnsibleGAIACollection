.. _cp_gaia_loopback_interface_facts_module:


cp_gaia_loopback_interface_facts -- Show loopback interface/s.
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show loopback interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    Interface name to show. If not specified, all loopback interfaces information is returned.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show loopback interface
      check_point.gaia.cp_gaia_loopback_interface_facts:

    - name: Show loopback interface by specifying it's name
      check_point.gaia.cp_gaia_loopback_interface_facts:
        name: loop01




Return Values
-------------

ansible_facts (always., dict, )
  The interface/s facts.


  objects (always, list, )
    List of interfaces.


    name (always, str, )
      Interface name.


    ipv4_address (always, str, )
      Interface IPv4 address.


    ipv4_mask_length (always, int, )
      Interface IPv4 address mask length.


    ipv6_address (always, str, )
      Interface IPv6 address.


    ipv6_autoconfig (always, bool, )
      Configure IPv6 auto-configuration.


    ipv6_mask_length (always, int, )
      Interface IPv6 address mask length.


    comments (always, str, )
      Interface Comments.


    enabled (always, bool, )
      Interface State.


    mtu (always, int, )
      Interface mtu.


    ipv6_local_link_address (always, str, )
      Interface ipv6 local link address.


    status (always, dict, )
      Interface data.


      link_state (always, bool, )
        Link status.


      speed (always, str, )
        Speed.


      duplex (always, str, )
        Duplex.


      tx_bytes (always, int, )
        TX bytes.


      tx_packets (always, int, )
        TX packets.


      rx_bytes (always, int, )
        RX bytes.


      rx_packets (always, int, )
        RX packets.








Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

