.. _cp_gaia_timezones_facts_module:


cp_gaia_timezones_facts -- Shows available areas and regions for timezone.
==========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Shows available areas and regions for timezone.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show timezones
      check_point.gaia.cp_gaia_timezones_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  timezones (always, list, )
    List of timezones in Area / Region format.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

