.. _cp_gaia_bridge_interface_facts_module:


cp_gaia_bridge_interface_facts -- Show bridge interface/s.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show bridge interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    Interface name to show. If not specified, all bridge interfaces information is returned.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show bridge interface
      check_point.gaia.cp_gaia_bridge_interface_facts:

    - name: Show bridge interface by specifying it's name
      check_point.gaia.cp_gaia_bridge_interface_facts:
        name: br1




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


    dhcp (always, dict, )
      DHCP configuration.


      enabled (always, bool, )
        Enable DHCP on this interface.


      server_timeout (always, int, )
        Specifies the amount of time, in seconds, that must pass between the time that the interface begins to try to determine its address and the time that it decides that it's not going to be able to contact a server.


      retry (always, int, )
        Specifies the time, in seconds, that must pass after the interface has determined that there is no DHCP server present before it tries again to contact a DHCP server.


      leasetime (always, int, )
        Specifies the lease time, in seconds, when requesting for an IP address. Default value is "default" - according to the server.


      reacquire_timeout (always, int, )
        When trying to reacquire the last ip address, The reacquire-timeout statement sets the time, in seconds, that must elapse after the first try to reacquire the old address before it gives up and tries to discover a new address.



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

- Ameer Asli (@chkp-ameera)

