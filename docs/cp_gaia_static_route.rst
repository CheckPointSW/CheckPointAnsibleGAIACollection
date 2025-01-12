.. _cp_gaia_static_route_module:


cp_gaia_static_route -- Modify the configuration of static route.
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify the configuration of static route.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  address (True, str, None)
    IPv4 address.


  mask_length (True, int, None)
    Mask length address.Valid values are 0-32.


  type (True, str, None)
    Type of next hop.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  next_hop (False, list, None)
    Static next\_hop. Contains a list of next-hop gateways.


    gateway (False, str, None)
      IP address or logical name for the static next-hop gateway.


    priority (False, int, None)
      Priority defines which gateway to select as the next-hop. The lower the priority, the higher the preference. Possible values are 1-8.



  comment (False, str, None)
    Static route comment.


  rank (False, int, None)
    Selects a route when there are many routes to a destination that use different routing protocols. The route with the lowest rank value is selected. Possible values are 0-255.


  ping (False, bool, False)
    Configures ping monitoring of the given IPv4 static route.


  scope_local (False, bool, False)
    Configure the local interface scope option, When the this option is enabled, the route treated as directly connected to local machine.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set new static route
      check_point.gaia.cp_gaia_static_route:
        state: present
        address: 1.2.125.0
        mask_length: 24
        type: gateway
        next_hop: [{"gateway": "1.1.1.1", "priority": 2}]




Return Values
-------------

static_route (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

