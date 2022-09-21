.. _cp_gaia_scheduled_snapshot_facts_module:


cp_gaia_scheduled_snapshot_facts -- Show the snapshot scheduler configuration.
==============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the snapshot scheduler configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show the snapshot scheduler configuration
      check_point.gaia.cp_gaia_scheduled_snapshot_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  description (always, str, )
    Description of the scheduled snapshot.


  enabled (always, bool, )
    State of the snapshot scheduler.


  retention_policy (always, dict, )
    Retention policy for the snapshot scheduler.


    keep_disk_space_above_in_GB (always, int, )
      Minimum diskspace to keep on the local machine (GB).


    min_snapshots_to_keep (always, int, )
      Minimum snapshots to keep.


    max_snapshots_to_keep (always, int, )
      Maximum snapshots to keep.



  recurrence (always, dict, )
    Recurrence of the scheduled snapshot.


    time (always, dict, )
      Recurrence time.


      hour (always, int, )
        Time hour.


      minute (always, int, )
        Time minute.



    pattern (always, str, )
      Recurrence pattern. choices=['daily', 'monthly', 'weekly'].


    months (always, list, )
      Recurrence months.


    weekdays (always, list, )
      Recurrence weekdays.


    days (always, list, )
      Recurrence days.



  name_prefix (always, str, )
    Prefix for the snapshots name created by the scheduler.


  host (always, dict, )
    Target host for the snapshots creation.


    username (always, str, )
      Username for scp/ftp targets.


    upload_path (always, str, )
      Upload path for scp/ftp targets.


    password (always, str, )
      Password for scp/ftp targets.


    target (always, str, )
      Host target type. choices=['lvm', 'ftp', 'scp'].


    ip_address (always, str, )
      IP_Address of the target.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

