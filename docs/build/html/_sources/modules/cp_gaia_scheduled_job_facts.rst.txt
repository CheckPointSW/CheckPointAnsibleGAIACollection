.. _cp_gaia_scheduled_job_facts_module:


cp_gaia_scheduled_job_facts -- Show scheduled job/s information.
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show scheduled job information.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    Scheduled job name to show. If not specified, all scheduled jobs information is returned.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show scheduled jobs
      check_point.gaia.cp_gaia_scheduled_job_facts:

    - name: Show scheduled job by specifying it's name
      check_point.gaia.cp_gaia_scheduled_job_facts):
        name: test_job




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  jobs (always, list, )
    All jobs.


    name (always, str, )
      Scheduled job name.


    command (always, str, )
      Command (expert CLI style).


    recurrence (always, dict, )
      Recurrence.


      type (always, str, )
        Job recurrence type.


      interval (always, int, )
        Time interval in minutes. Relevant for "interval" recurrence type.


      time_of_day (always, dict, )
        Time of day in 24 hour format. Relevant for "daily", "weekly" and "monthly" recurrence types.


        hour (always, int, )
          Time hour.


        minute (always, int, )
          Time minute.



      hourly (always, dict, )
        Hours of day in 24 hour format. Can choose multiple hours. Relevant for "hourly" recurrence type.


        hours_of_day (always, list, )
          Hours of day in 24 hour format.


        minute (always, int, )
          Time minute.



      weekdays (always, list, )
        Days of the week. Relevant for "weekly" recurrence type.


      days (always, list, )
        Days of the month. Relevant for "monthly" recurrence type.


      months (always, list, )
        Month numbers. Relevant for "monthly" recurrence type.








Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

