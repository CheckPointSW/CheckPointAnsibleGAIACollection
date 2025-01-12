.. _cp_gaia_diagnostics_topics_facts_module:


cp_gaia_diagnostics_topics_facts -- Show diagnostics topics.
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show diagnostics topics.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



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

    
    - name: Show diagnostics_topics
      check_point.gaia.cp_gaia_diagnostics_topics_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The diagnostics topics facts.


  os (always, list, )
    The topics which are valid for show-diagnostics.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

