.. _cp_gaia_remote_syslog_facts_module:


cp_gaia_remote_syslog_facts -- Show remote system log server configuration.
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show remote system log server configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  server_ip (False, str, None)
    No Documentation available.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show remote syslog log server by specifying it IP
      check_point.gaia.cp_gaia_remote_syslog_facts:
        server_ip: "10.11.2.130"




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  server_ip (always, str, )
    No Documentation available.


  state (always, str, )
    Ansible state which can be ``present`` or ``absent``.


  protocol (always, str, )
    Log protocol, Supported starting from R81.20 .


  port (always, str, )
    Log port, Supported starting from R81.20 .


  level (always, str, )
    No Documentation available.






Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

