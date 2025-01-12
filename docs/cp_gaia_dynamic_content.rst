.. _cp_gaia_dynamic_content_module:


cp_gaia_dynamic_content -- installing policy
============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Installing policy






Parameters
----------

  version (False, str, None)
    GAIA api version for ex 1.8


  policy_path (True, str, None)
    path for the policy json


  dry_run (True, bool, None)
    dry\_run set to true will apply the change, wheres set to false it will only validate the changes


  tags (True, list, None)
    list of tags for the operation


  comments (True, str, None)
    comments for the operation


  wait_for_task (False, bool, False)
    Wait for task or return immediately.





Notes
-----

.. note::
   - its advisable to perform with wait\_for\_task set to false and refer to show\_task command




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Initial setup
      check_point.gaia.cp_gaia_dynamic_content:
        policy_path: "/home/admin/policy.json"
        dry_run: false
        tags: ["JIRA-12345", "apply layer1"]
        comments: "testing the api"
        wait_for_task: true



Return Values
-------------

change_summary (always., dict, )
  change-summary after installing the new policy.





Status
------





Authors
~~~~~~~

- Ophir Khill (@chkp-ophirk)

