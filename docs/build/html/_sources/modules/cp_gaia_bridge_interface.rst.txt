.. _cp_gaia_bridge_interface_module:


cp_gaia_bridge_interface -- Modify bridge interface.
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify bridge interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be ``present`` or ``absent``.


  name (True, str, None)
    Interface name with format ``br<id>``, valid values are br1, br2, br3 .. etc.


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


  comments (False, str, None)
    Interface Comments.


  enabled (False, bool, None)
    Interface State.


  dhcp (False, dict, None)
    DHCP configuration.


    enabled (False, bool, None)
      Enable DHCP on this interface.


    server_timeout (False, int, 60)
      Specifies the amount of time, in seconds, that must pass between the time that the interface begins to try to determine its address and the time that it decides that it's not going to be able to contact a server.


    retry (False, int, 300)
      Specifies the time, in seconds, that must pass after the interface has determined that there is no DHCP server present before it tries again to contact a DHCP server.


    leasetime (False, int, None)
      Specifies the lease time, in seconds, when requesting for an IP address. Default value is ``default`` - according to the server.


    reacquire_timeout (False, int, 10)
      When trying to reacquire the last ip address, The reacquire-timeout statement sets the time, in seconds, that must elapse after the first try to reacquire the old address before it gives up and tries to discover a new address.



  mtu (False, int, None)
    Interface mtu.


  members (False, list, None)
    Interfaces members of the bridge.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add new bridge interface
      check_point.gaia.cp_gaia_bridge_interface:
        comments: bridge5 interface
        name: br5
        members: ['eth3', 'eth4']




Return Values
-------------

bridge_interface (always., dict, )
  The updated interface details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

