.. _cp_gaia_scheduled_job_module:


cp_gaia_scheduled_job -- Modify scheduled job.
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change the scheduled job's recurrence or command. Scheduled jobs run as admin.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (True, str, None)
    Scheduled job name.


  command (False, str, None)
    Command (expert CLI style).


  recurrence (False, dict, None)
    Recurrence.


    type (False, str, None)
      Job recurrence type.


    interval (False, int, None)
      Time interval in minutes. Relevant for "interval" recurrence type.


    time_of_day (False, dict, None)
      Time of day in 24 hour format. Relevant for "daily", "weekly" and "monthly" recurrence types.


      hour (False, int, None)
        Time hour.


      minute (False, int, None)
        Time minute.



    hourly (False, dict, None)
      Hours of day in 24 hour format. Can choose multiple hours. Relevant for "hourly" recurrence type.


      hours_of_day (False, list, None)
        Hours of day in 24 hour format.


      minute (False, int, None)
        Time minute.



    weekdays (False, list, None)
      Days of the week. Relevant for "weekly" recurrence type.


    days (False, list, None)
      Days of the month. Relevant for "monthly" recurrence type.


    months (False, list, None)
      Month numbers. Relevant for "monthly" recurrence type.






Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add new scheduled job
      check_point.gaia.cp_gaia_scheduled_job:
        name: "startup_job"
        command: "/home/admin/job.sh"
        recurrence: {"type": "system-startup"}




Return Values
-------------

scheduled_job (always., dict, )
  The updated scheduled job details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

