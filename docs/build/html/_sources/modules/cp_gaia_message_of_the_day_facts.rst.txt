.. _cp_gaia_message_of_the_day_facts_module:


cp_gaia_message_of_the_day_facts -- Show message of the day settings.
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show message of the day settings.



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

    
    - name: Show message of the day
      check_point.gaia.cp_gaia_message_of_the_day_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  enabled (always, bool, )
    Message of the day enabled (true/false).


  message (always, str, )
    Message of the day for web, ssh and serial login.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

