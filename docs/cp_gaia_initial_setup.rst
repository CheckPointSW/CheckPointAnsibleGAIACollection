.. _cp_gaia_initial_setup_module:


cp_gaia_initial_setup -- Run First Time Wizard configuration.
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Run First Time Wizard configuration.






Parameters
----------

  wait_for_task (False, bool, True)
    Wait for task or return immediately.


  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  password (False, str, None)
    Password of user admin. Required in case default initial password has not been changed before.


  security_management (False, dict, None)
    Install Security Management or Multi domain server.


    multi_domain (False, bool, False)
      Install Security Multi domain server, it can be :literal:`primary` or :literal:`secondary` or :literal:`log-server` according to type parameter.


    type (False, str, primary)
      Type of security management or multi domain server.


    activation_key (False, str, None)
      Secure Internal Communication key, relevant in case of secondary or log-server.


    leading_interface (False, str, None)
      Leading multi domain server interface, relevant in case of multi-domain enabled.


    gui_clients (False, dict, None)
      Choose which GUI clients can log into the Security Management. fill one of the parameters :literal:`range` :literal:`network` :literal:`single-ip`\ , for multi-domain it can be only single-ip or can keep the default value.


      range (False, dict, None)
        Range of IPs allowed to connect to management.


        first_IPv4_range (False, str, None)
          First IP in range.


        last_IPv4_range (False, str, None)
          Last IP in range.



      network (False, dict, None)
        IPs from specific network allowed to connect to management.


        address (False, str, None)
          IPv4 address of network.


        mask_length (False, int, None)
          Mask length of network.



      single_ip (False, str, None)
        In case of a single IP which allowed to connect to management.




  security_gateway (False, dict, None)
    Install Security Gateway.


    dynamically_assigned_ip (False, bool, False)
      Enable DAIP (dynamic ip) gateway. Should be false if cluster\_member or security\_management enabled.


    cluster_member (False, bool, False)
      Enable/Disable ClusterXL.


    activation_key (False, str, None)
      Secure Internal Communication key.


    vsnext (False, bool, False)
      Enable/Disable VSNext.


    elastic_xl (False, bool, False)
      Enable/Disable ElasticXL.






Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Initial setup
      check_point.gaia.cp_gaia_initial_setup:
        wait_for_task: true
        security_gateway: {cluster_member: false, activation_key: bbbb, dynamically_assigned_ip: false}



Return Values
-------------

initial_setup (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

