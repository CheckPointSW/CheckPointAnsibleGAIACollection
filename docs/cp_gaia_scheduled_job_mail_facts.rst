.. _cp_gaia_scheduled_job_mail_facts_module:


cp_gaia_scheduled_job_mail_facts -- Show scheduled job mail information.
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show scheduled job mail information.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



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

    
    - name: Show scheduled job mail
      check_point.gaia.cp_gaia_scheduled_job_mail_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  email_address (always., str, )
    E-mail address to send reports to.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

