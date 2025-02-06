.. _cp_gaia_maestro_changes_module:


cp_gaia_maestro_changes -- Handle pending changes, either apply or delete them.
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Handle pending changes, either apply or delete them.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be :literal:`present` or :literal:`absent`. absent will delete the pending changes, present will apply them


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Delete pending changes
      check_point.gaia.cp_gaia_user:
        state: absent





Status
------





Authors
~~~~~~~

- Roi Tal (@chkp-roital)

