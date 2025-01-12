.. _cp_gaia_syslog_facts_module:


cp_gaia_syslog_facts -- Show system log configuration.
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show system log configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show system logging configuration
      check_point.gaia.cp_gaia_syslog_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  send_to_mgmt (always., bool, )
    Sending logs to Management server.


  cp_logs (always., bool, )
    Syslog auditlog permanent.


  audit_log (always., bool, )
    Syslog auditlog permanent.


  filename (always., str, )
    Syslog output filename.






Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

