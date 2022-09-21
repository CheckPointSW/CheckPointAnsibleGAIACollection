.. _cp_gaia_run_reboot_module:


cp_gaia_run_reboot -- Run reboot on Check Point machine.
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Reboot Check Point machine operation.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Run reboot
      check_point.gaia.cp_gaia_run_reboot:



Return Values
-------------

run_reboot (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

