.. _cp_gaia_vsnext_state_facts_module:


cp_gaia_vsnext_state_facts -- Show the VSNext state.
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the VSNext state.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.8.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show VSNext state
      check_point.gaia.cp_gaia_vsnext_state_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The VSNext state facts.


  enabled (always, bool, )
    The VSNext state.


  session-virtual-system-id (always, int, )
    The Virtual System ID of the current Gaia API session.


  member-id (On Scalable and Elastic XL platforms only., int, )
    The member on which the command was executed.






Status
------





Authors
~~~~~~~

- Omer Hadad (@chkp-omerhad)

