.. _cp_gaia_dynamic_content_layers_facts_module:


cp_gaia_dynamic_content_layers_facts -- get the names and meta-data of all dynamic layers.
==========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

get the names and metadata of all dynamic layers






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: show dynamic layers
      check_point.gaia.cp_gaia_dynamic_content_layers_facts:



Return Values
-------------

hostname (always., dict, )
  the names and metadata of all dynamic layers.





Status
------





Authors
~~~~~~~

- Ophir Khill (@chkp-ophirk)

