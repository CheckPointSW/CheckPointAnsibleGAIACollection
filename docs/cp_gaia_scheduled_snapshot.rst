.. _cp_gaia_scheduled_snapshot_module:


cp_gaia_scheduled_snapshot -- Set scheduled snapshot.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set scheduled snapshot.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  description (False, str, None)
    Description of the scheduled snapshot.


  enabled (False, bool, None)
    State of the snapshot scheduler.


  retention_policy (False, dict, None)
    Retention policy for the snapshot scheduler.


    keep_disk_space_above_in_GB (False, int, None)
      Minimum diskspace to keep on the local machine (GB).


    min_snapshots_to_keep (False, int, None)
      Minimum snapshots to keep.


    max_snapshots_to_keep (False, int, None)
      Maximum snapshots to keep.



  recurrence (False, dict, None)
    Recurrence of the scheduled snapshot.


    time (False, dict, None)
      Recurrence time.


      hour (False, int, None)
        Time hour.


      minute (False, int, None)
        Time minute.



    pattern (False, str, None)
      Recurrence pattern. choices=['daily', 'monthly', 'weekly'].


    months (False, list, None)
      Recurrence months.


    weekdays (False, list, None)
      Recurrence weekdays.


    days (False, list, None)
      Recurrence days.



  name_prefix (False, str, None)
    Prefix for the snapshots name created by the scheduler.


  host (False, dict, None)
    Target host for the snapshots creation.


    username (False, str, None)
      Username for scp/ftp targets.


    upload_path (False, str, None)
      Upload path for scp/ftp targets.


    password (False, str, None)
      Password for scp/ftp targets.


    target (False, str, None)
      Host target type. choices=['lvm', 'ftp', 'scp'].


    ip_address (False, str, None)
      IP\_Address of the target.






Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set scheduled snapshot
      check_point.gaia.cp_gaia_scheduled_snapshot:
        recurrence: {"pattern": "weekly", "weekdays": ["Mon","Wed"], time: {"minute": 30,"hour": 13}}
        name_prefix: "weeklySnap"
        host: {"username": "username","upload_path": "/home/admin/", "password": "secret", "target": "lvm"}
        enabled: True
        description: "weekly"



Return Values
-------------

scheduled_snapshot (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

