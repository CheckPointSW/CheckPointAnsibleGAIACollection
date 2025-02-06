.. _cp_gaia_simulate_packet_module:


cp_gaia_simulate_packet -- installing policy
============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

simulate packet execution on both Access and NAT rulebase.






Parameters
----------

  version (False, str, None)
    GAIA api version for ex 1.8


  virtual_system_id (False, int, None)
    Virtual System ID.


  ip_version (False, str, 4)
    ip version of the packet.


  source_ip (True, str, None)
    source ip of the packet.


  destination_ip (True, str, None)
    destination ip of the packet.


  ip_protocol (True, str, None)
    destination ip of the packet.


  protocol_options (True, dict, None)
    protocol specific options.


    UDP (False, dict, None)
      UDP specific options.


      source_port (False, str, 12345)
        source port of the packet.


      destination_port (True, str, None)
        destination port of the packet.



    TCP (False, dict, None)
      TCP specific options.


      source_port (False, str, 12345)
        source port of the packet.


      destination_port (True, str, None)
        destination port of the packet.



    icmp (False, dict, None)
      ICMP specific options.


      type (True, str, None)
        source port of the packet.


      code (False, str, 0)
        destination port of the packet.




  incoming_interface (True, str, None)
    packet's incoming interface, set to 'localhost' for outbound packets.


  application (False, list, None)
    list of Applications/Categorys as defined in SmartConsole. You can specify one or more applications


  protocol (False, str, None)
    Protocol to match for services that have 'Protocol Signature' enabled.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - its advisable to perform with wait\_for\_task set to false and refer to show\_task command




Examples
--------

.. code-block:: yaml+jinja

    
    - name: simulate packet
      check_point.gaia.cp_gaia_simulate_packet:
        ip_version: "4"
        source_ip: "1.2.3.4"
        destination_ip: "2.3.4.5"
        ip_protocol: "1"
        protocol_options: {icmp: {type: "8"}}
        incoming_interface: "eth0"
        application: "Facebook"
        protocol: "HTTP"



Return Values
-------------

packet rulebase execution result (always., dict, )
  the NAT and Access rulebase execution result.





Status
------





Authors
~~~~~~~

- Ophir Khill (@chkp-ophirk)

