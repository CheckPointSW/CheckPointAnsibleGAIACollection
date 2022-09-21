.. _cp_gaia_syslog_module:


cp_gaia_syslog -- Setting system logging configuration.
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting system logging configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  send_to_mgmt (False, bool, None)
    Sending logs to Management server.


  cp_logs (False, bool, None)
    Syslog auditlog permanent.


  audit_log (False, bool, None)
    Syslog auditlog permanent.


  filename (False, str, None)
    Syslog output filename.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Modify system logging configuration
      check_point.gaia.cp_gaia_syslog:
        send_to_mgmt: false
        filename: "/var/log/messages"
        cp_logs: false
        audit_log: true




Return Values
-------------

syslog (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

