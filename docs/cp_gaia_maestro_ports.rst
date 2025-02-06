.. _cp_gaia_maestro_ports_module:


cp_gaia_maestro_ports -- Set Port configuration.
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Port configuration. Note that at least one of 'id' or 'interface-name' must be provided.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  id (False, str, None)
    Port ID (e.g. '1/13/1').


  interface_name (False, str, None)
    Interface name in case this port is an Uplink or MGMT interface (e.g. 'eth1-25').


  enabled (False, bool, None)
    Setting this to false will disable this port, setting to true will enable it. AKA 'admin state'.


  mtu (False, int, None)
    MTU of this port.


  auto_negotiation (False, bool, None)
    If true, Auto Negotiation will be turned on, and vice versa.


  qsfp_mode (False, str, None)
    Port QSFP mode.


  type (False, str, None)
    Port type.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change port QSFP mode
      check_point.gaia.cp_gaia_ports:
        id: 1/1/1
        qsfp_mode: 4x25G



Return Values
-------------

maestro_port (always., dict, )
  The updated Port details.





Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

