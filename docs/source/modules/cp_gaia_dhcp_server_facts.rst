.. _cp_gaia_dhcp_server_facts_module:


cp_gaia_dhcp_server_facts -- Shows DHCP server information.
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Shows DHCP server information.






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

    
    - name: Shows DHCP server information.
      check_point.gaia.cp_gaia_dhcp_server_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The interface/s facts.


  enabled (always, bool, )
    DHCP server status.


  subnets (always, list, )
    Subnets.


    subnet (always, str, )
      IPv4 address for the subnet.


    max_lease (always, int, )
      The longest lease that the server can allocate, in seconds.


    default_lease (always, int, )
      The default lease that the server allocates, in seconds.


    enabled (always, bool, )
      Enable DHCP on this subnet.


    ip_pools (always, list, )
      Range of IPv4 addresses that the server assigns to hosts.


      start (always, str, )
        The first IPv4 address of the range.


      include (always, str, )
        Specifies whether to include or exclude this range of IPv4 addresses in the IP pool.


      end (always, str, )
        The last IPv4 address of the range.


      enabled (always, bool, )
        Enables or disables the DHCP Server for this subnet IP pool.



    netmask (always, int, )
      Subnet mask.


    default_gateway (always, str, )
      The IPv4 address of the default gateway for the DHCP clients.


    dns (always, dict, )
      DNS configuration.


      domain_name (always, str, )
        Domain name.


      primary (always, str, )
        The IPv4 address of the Primary DNS server for the DHCP clients.


      secondary (always, str, )
        The IPv4 address of the Secondary DNS server for the DHCP clients (to use if the primary DNS server does not respond).


      tertiary (always, str, )
        The IPv4 address of the Tertiary DNS server for the DHCP clients (to use if the primary and secondary DNS servers do not respond).








Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

