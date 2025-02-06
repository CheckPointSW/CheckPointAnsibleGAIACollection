.. _cp_gaia_physical_interface_module:


cp_gaia_physical_interface -- Set Physical interface.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Physical interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  auto_negotiation (False, bool, None)
    Activating Auto-Negotiation will skip the speed and duplex configuration.


  comments (False, str, None)
    Interface Comments.


  duplex (False, str, None)
    Duplex for the interface. Duplex is not relevant when 'auto-negotiation' is enabled.


  enabled (False, bool, None)
    Interface State.


  ipv4_address (False, str, None)
    Interface IPv4 address.


  ipv4_mask_length (False, int, None)
    Interface IPv4 address mask length.


  ipv6_address (False, str, None)
    Interface IPv6 address.


  ipv6_autoconfig (False, bool, None)
    Configure IPv6 auto-configuration.


  ipv6_mask_length (False, int, None)
    Interface IPv6 address mask length.


  mac_addr (False, str, None)
    Configure hardware address.


  monitor_mode (False, bool, None)
    Set monitor mode for the interface off/on.


  mtu (False, int, None)
    Interface mtu.


  name (True, str, None)
    Interface name.


  rx_ringsize (False, int, None)
    Set receive buffer size for interface.


  speed (False, str, None)
    Interface link speed. Speed is not relevant when 'auto-negotiation' is enabled.


  tx_ringsize (False, int, None)
    Set transmit buffer size for interfaces.


  dhcp (False, dict, None)
    DHCP configuration.


    enabled (False, bool, None)
      Enable DHCP on this interface.


    server_timeout (False, int, 60)
      Specifies the amount of time, in seconds, that must pass between the time that the interface begins to try to determine its address and the time that it decides that it's not going to be able to contact a server.


    retry (False, int, 300)
      Specifies the time, in seconds, that must pass after the interface has determined that there is no DHCP server present before it tries again to contact a DHCP server.


    leasetime (False, int, None)
      Specifies the lease time, in seconds, when requesting for an IP address. Default value is "default" - according to the server.


    reacquire_timeout (False, int, 10)
      When trying to reacquire the last ip address, The reacquire-timeout statement sets the time, in seconds, that must elapse after the first try to reacquire the old address before it gives up and tries to discover a new address.






Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set comment field of a physical interface
      check_point.gaia.cp_gaia_physical_interface:
        comments: eth0 interface
        enabled: true
        name: eth0



Return Values
-------------

physical_interface (always., dict, )
  The updated interface details.





Status
------





Authors
~~~~~~~

- Yuval Feiger (@chkp-yuvalfe)

