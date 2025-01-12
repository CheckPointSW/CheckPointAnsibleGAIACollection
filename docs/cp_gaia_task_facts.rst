.. _cp_gaia_task_facts_module:


cp_gaia_task_facts -- Show task.
================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show task.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  task_id (True, list, None)
    List of task ids to show.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show task
      check_point.gaia.cp_gaia_task_facts:
        task_id: ["ccc88f8f-ee65-44d2-bdc6-797f8347f6e1"]



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  tasks (always, list, )
    Tasks.


    task_id (always, str, )
      ID of the task being executed.


    last_update_time (always, str, )
      Last update timestamp from task's execution. A task can update its status during execution. Updates interval will change from one API to another.


    progress_description (always, str, )
      Progress description will change between one API to another.


    progress_percentage (always, int, )
      Note Percentage will be marked as 100 upon failure as well.


    start_time (always, str, )
      Execution start time, in iso8601 format.


    status_code (always, int, )
      HTTP return code.


    task_name (always, str, )
      Request URL. For example '/run-script' for run-script tasks.


    status (always, str, )
      Status.


    task_details (always, list, )
      The type of object depends on the request. See 'run-script' output for example.


    execution_time (always, int, )
      Time in seconds.


    time_spent_in_queue (always, int, )
      Time in seconds.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

