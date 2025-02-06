.. _cp_gaia_scheduled_job_mail_module:


cp_gaia_scheduled_job_mail -- Modify scheduled job mail.
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set which e-mail address the job scheduler sends reports to. Pass empty string to delete the current e-mail address.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  email_address (True, str, None)
    E-mail address to send reports to.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set scheduled job mail
      check_point.gaia.cp_gaia_scheduled_job_mail:
        email_address: "sysadmins@company.com"



Return Values
-------------

scheduled_job_mail (always., dict, )
  The updated scheduled job mail.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

