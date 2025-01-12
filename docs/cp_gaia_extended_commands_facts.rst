.. _cp_gaia_extended_commands_facts_module:


cp_gaia_extended_commands_facts -- Show available extended commands.
====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show available extended commands.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show extended commands
      check_point.gaia.cp_gaia_extended_commands_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The extended commands facts.


  extended_commands (always, list, )
    Available extended commands.


    name (always, str, )
      Extended command name.


    description (always, str, )
      Extended command description.


    path (always, str, )
      Extended command path.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

