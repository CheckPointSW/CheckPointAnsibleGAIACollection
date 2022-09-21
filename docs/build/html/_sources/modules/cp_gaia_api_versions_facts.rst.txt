.. _cp_gaia_api_versions_facts_module:


cp_gaia_api_versions_facts -- Show api versions.
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show api versions.



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

    
    - name: Show api versions
      check_point.gaia.cp_gaia_api_versions_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The api versions facts.


  current_version (always, str, )
    Represents the latest supported version by the installed REST engine.


  supported_versions (always, list, )
    Represents all the previous versions supported by the installed REST engine.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

