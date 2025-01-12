.. _cp_gaia_diagnostics_facts_module:


cp_gaia_diagnostics_facts -- Show diagnostics.
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show diagnostics.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  category (True, str, None)
    Category.


  topic (True, str, None)
    Category.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show diagnostics
      check_point.gaia.cp_gaia_diagnostics_facts:
        category: os
        topic: memory



Return Values
-------------

ansible_facts (always., dict, )
  The diagnostics facts.


  total (always, int, )
    How much to show.


  from (always, int, )
    Starting from.


  to (always, int, )
    Ending to.


  objects (always, list, )
    List for memory, disk, or CPU based on the "topic" parameter.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

