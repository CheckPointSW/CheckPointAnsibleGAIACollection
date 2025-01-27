.. _cp_gaia_virtual_switch_facts_module:


cp_gaia_virtual_switch_facts -- Get virtual-switch objects facts on Check Point over Web Services API
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get virtual-switch objects facts on Check Point devices.

All operations are performed over Web Services API.

This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter 'id' to specify the virtual switch id.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.8.


  virtual_system_id (False, int, None)
    Virtual System ID.


  id (optional, int, None)
    Virtual Switch ID. This parameter is relevant only for getting a specific Virtual Switch object.


  member_id (optional, int, None)
    The member on which the command is executed.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: show-virtual-switch
      cp_gaia_virtual_switch_facts:
        id: 1
    - name: show-virtual-switches
      cp_gaia_virtual_switch_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.





Status
------





Authors
~~~~~~~

- Omer Hadad (@chkp-omerhad)

