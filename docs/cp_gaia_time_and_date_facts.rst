.. _cp_gaia_time_and_date_facts_module:


cp_gaia_time_and_date_facts -- Show the time and date configuration.
====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the time and date configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.7.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show time and date configuration
      check_point.gaia.cp_gaia_time_and_date_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  time (always, str, )
    Time in HH:MM:SS format.


  date (always, str, )
    Date in DD-MM-YYYY format.


  timezone (always, str, )
    Timezone in Area/Region format.


  iso8601 (always, str, )
    Time information in iso 8601 format.


  posix (always, int, )
    Time information in posix format.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

