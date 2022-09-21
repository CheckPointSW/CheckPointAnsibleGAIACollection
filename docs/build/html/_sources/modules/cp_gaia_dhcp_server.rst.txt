.. _cp_gaia_dhcp_server_module:


cp_gaia_dhcp_server -- Change DHCP server settings.
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change DHCP server settings.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  enabled (False, bool, None)
    DHCP server status.


  subnets (False, list, None)
    Subnets.


    subnet (False, str, None)
      IPv4 address for the subnet.


    max_lease (False, int, 86400)
      The longest lease that the server can allocate, in seconds.


    default_lease (False, int, 43200)
      The default lease that the server allocates, in seconds.


    enabled (False, bool, None)
      Enable DHCP on this subnet.


    ip_pools (False, list, None)
      Range of IPv4 addresses that the server assigns to hosts.


      start (False, str, None)
        The first IPv4 address of the range.


      include (False, str, None)
        Specifies whether to include or exclude this range of IPv4 addresses in the IP pool.


      end (False, str, None)
        The last IPv4 address of the range.


      enabled (False, bool, None)
        Enables or disables the DHCP Server for this subnet IP pool.



    netmask (False, int, None)
      Subnet mask.


    default_gateway (False, str, None)
      The IPv4 address of the default gateway for the DHCP clients.


    dns (False, dict, None)
      DNS configuration.


      domain_name (False, str, None)
        Domain name.


      primary (False, str, None)
        The IPv4 address of the Primary DNS server for the DHCP clients.


      secondary (False, str, None)
        The IPv4 address of the Secondary DNS server for the DHCP clients (to use if the primary DNS server does not respond).


      tertiary (False, str, None)
        The IPv4 address of the Tertiary DNS server for the DHCP clients (to use if the primary and secondary DNS servers do not respond).







Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change DHCP server settings
      check_point.gaia.cp_gaia_dhcp_server:
        enabled: False
        subnets: [
            {"subnet": "4.5.6.0",
            "netmask": 24,
            "max_lease": 86400,
            "default_lease": 43200,
            "default_gateway": "4.5.6.1",
            "ip_pools": [{"start": "4.5.6.5", "end": "4.5.6.7", "enabled": True, "include": "include"}],
            "dns": {"domain_name": "my_domain_name", "primary": "8.8.8.8", "secondary": "8.8.8.8", "tertiary": "8.8.4.4"},
            "enabled": True}
        ]



Return Values
-------------

dhcp_server (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

