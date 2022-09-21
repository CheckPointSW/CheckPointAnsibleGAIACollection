.. _cp_gaia_remote_syslog_module:


cp_gaia_remote_syslog -- Modify remote system log server configuration.
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify remote system log server configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  server_ip (True, str, None)
    No Documentation available.


  state (False, str, present)
    Ansible state which can be ``present`` or ``absent``.


  protocol (False, str, None)
    Log protocol, Supported starting from R81.20 .


  port (False, str, None)
    Log port, Supported starting from R81.20 .


  level (False, str, None)
    No Documentation available.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Modifying remote syslog messaging level
      check_point.gaia.cp_gaia_remote_syslog:
        server_ip: "10.11.2.130"
        level: "debug"




Return Values
-------------

remote_syslog (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

