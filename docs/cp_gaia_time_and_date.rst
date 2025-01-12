.. _cp_gaia_time_and_date_module:


cp_gaia_time_and_date -- Show the time and date configuration.
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the time and date configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.7.


  time (False, str, None)
    Time to set, in HH:MM[:SS] format.


  date (False, str, None)
    Date to set, in YYYY-MM-DD format.


  timezone (False, str, None)
    Timezone in Area / Region format. See timezone list via cp\_gaia\_timezones\_facts.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Setting new time and date
      check_point.gaia.cp_gaia_time_and_date:
        time: newpass
        date: newpass
        timezone: newpass



Return Values
-------------

set_time_and_date (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

