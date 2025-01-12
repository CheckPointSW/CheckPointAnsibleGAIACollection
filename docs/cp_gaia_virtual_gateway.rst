.. _cp_gaia_virtual_gateway_module:


cp_gaia_virtual_gateway -- Manages virtual gateway on Check Point Gateway over Web Services API
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manages virtual gateway on Check Point gateways including creating, updating, and removing virtual systems.

All operations are performed over Web Services API.






Parameters
----------

  id (optional, str, None)
    Virtual gateway ID.

    This parameter is used to change an existing virtual gateway or create a new one if it does not exist.


  name (optional, str, None)
    Name of the virtual gateway.

    This parameter is used to change an existing virtual gateway by name.


  one_time_password (optional, str, None)
    One-time password of the virtual gateway.

    This parameter is used to set the one-time password for an existing virtual gateway by name or ID.


  interfaces (optional, list, None)
    Configure interfaces for the virtual gateway.

    Collection of interfaces to be set, identified by the name. Replaces existing interfaces.


  resources (optional, dict, None)
    Virtual gateway resources configuration.


    firewall_ipv4_instances (optional, int, None)
      The number of IPv4 CoreXL instances to be assigned to the virtual gateway identified by name or ID.


    firewall_ipv6_instances (optional, int, None)
      The number of IPv6 CoreXL instances to be assigned to the virtual gateway identified by name or ID.



  virtual_switches (optional, list, None)
    Connect virtual gateway identified by name or ID to pre-existing virtual switches identified by their IDs.

    Collection of virtual switches to be set, identified by their IDs. Replaces existing interfaces.


  mgmt_connection (optional, dict, None)
    Management connection configuration.


    mgmt_connection_identifier (optional, str, None)
      Management connection identifier.

      This parameter is used to change an existing virtual gateway by name.


    mgmt_connection_type (optional, str, None)
      Management connection type.

      This parameter is used to change an existing virtual gateway by name.


    mgmt_ipv4_configuration (optional, dict, None)
      Management connection IPv4 configuration.


      ipv4_address (optional, str, None)
        Management connection IPv4 address.


      ipv4_mask_length (optional, int, None)
        Management connection IPv4 mask length.


      ipv4_default_gateway (optional, str, None)
        Management connection IPv4 default gateway.



    mgmt_ipv6_configuration (optional, dict, None)
      Management connection IPv6 configuration.


      ipv6_address (optional, str, None)
        Management connection IPv6 address.


      ipv6_mask_length (optional, int, None)
        Management connection IPv6 mask length.


      ipv6_default_gateway (optional, str, None)
        Management connection IPv6 default gateway.











Examples
--------

.. code-block:: yaml+jinja

    
    - name: set virtual gateway
      check_point.gaia.cp_gaia_virtual_gateway:
        id: 11
        one_time_password: dummyOTP
        interfaces:
          - name: eth1-02.2
          - name: eth1-02.3
        virtual_switches:
          - id: 1
          - id: 500
        resources:
          firewall_ipv4_instances: 2
          firewall_ipv6_instances: 0
        mgmt_connection:
          mgmt_connection_identifier: 500
          mgmt_connection_type: virtual-switch-id
          mgmt_ipv4_configuration:
            ipv4_address: 172.72.72.1
            ipv4_mask: 24
            ipv4_default_gateway: 172.72.72.4



Return Values
-------------

cp_gaia_virtual_system (always., dict, )
  virtual gateway creation output.





Status
------





Authors
~~~~~~~

- Omer Hadad (@chkp-omerhad)

