.. _cp_gaia_virtual_switch_module:


cp_gaia_virtual_switch -- Manages virtual switch on Check Point Gateway over Web Services API
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manages virtual switches on Check Point gateways, including creating, updating, and removing virtual switches.

All operations are performed over the Web Services API.






Parameters
----------

  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  version (False, str, None)
    Gaia API version for example 1.8.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.


  virtual_system_id (False, int, None)
    Virtual System ID.


  id (optional, str, None)
    Virtual Switch ID.

    This parameter is used to change an existing virtual switch or create a new one if it does not exist.


  name (optional, str, None)
    Name of the virtual switch.

    This parameter is used to change an existing virtual switch or create a new one if it does not exist.


  interfaces (optional, list, None)
    Collection of interfaces to be set, identified by their names. Replaces existing interfaces.


    name (optional, str, None)
      Interface name.










Examples
--------

.. code-block:: yaml+jinja

    
    - name: set virtual switch
      check_point.gaia.cp_gaia_virtual_switch:
        id: 10
        name: AnsibleSwitch
        interfaces:
          - name: eth1-01
          - name: eth2.300
          - name: bond1.20



Return Values
-------------

cp_gaia_virtual_switch (always., dict, )
  virtual switch creation output.





Status
------





Authors
~~~~~~~

- Omer Hadad (@chkp-omerhad)

