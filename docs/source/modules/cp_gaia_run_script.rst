.. _cp_gaia_run_script_module:


cp_gaia_run_script -- Run script Check Point machine.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Run script on Check Point machine.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  script (True, str, None)
    Script body. Limited by 1300000 characters.


  description (False, str, None)
    Script description.


  args (False, str, None)
    Script arguments, separated by space character. Note don't send sensitive data on this parameter.


  environment_variables (False, list, None)
    Define environment variables to be used in the script, it's better to send sensitive data on environment variables since it's not stored.


    name (False, str, None)
      Variable's name.


    value (False, str, None)
      Variable's value.



  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Run script
      check_point.gaia.cp_gaia_run_script:
        script: "ls -la"
        environment_variables: [{"name": "VAR_NAME", "value": "VAR_VALUE"}]



Return Values
-------------

run_script (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

