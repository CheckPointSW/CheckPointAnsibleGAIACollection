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





Notes
-----

.. note::
   - Supports ``check_mode``.




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

