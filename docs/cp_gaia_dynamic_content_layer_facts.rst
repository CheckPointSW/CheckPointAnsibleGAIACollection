.. _cp_gaia_dynamic_content_layer_facts_module:


cp_gaia_dynamic_content_layer_facts -- getting information of the chosen dynamic layer.
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

getting information of a chosen dynamic layer.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  name (True, str, None)
    dynamic layer to show


  wait_for_task (False, bool, True)
    Wait for task or return immediately.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: show dynamic layer
      check_point.gaia.cp_gaia_dynamic_content_layer_facts:
        name: dynamic_layer



Return Values
-------------

layer_summary (always., dict, )
  the details of the installed policy on the requested layer





Status
------





Authors
~~~~~~~

- Ophir Khill (@chkp-ophirk)

