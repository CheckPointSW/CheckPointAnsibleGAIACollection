.. _cp_gaia_features_facts_module:


cp_gaia_features_facts -- Show available features.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show available features.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.7



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

    
    - name: Show features
      check_point.gaia.cp_gaia_features_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The features facts.


  features (always, list, )
    Available features.


    name (always, str, )
      feature name.


    description (always, str, )
      feature description.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

