.. _cp_gaia_message_of_the_day_module:


cp_gaia_message_of_the_day -- Setting the message of the day of a machine.
==========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting message of the day.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  msg (False, str, None)
    New message of the day for web, ssh and serial login.


  enabled (False, bool, None)
    Enable/Disable message of the day.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - message_of_the_day: Changing the message of the day
      check_point.gaia.cp_gaia_message_of_the_day:
        msg: "Hello today"




Return Values
-------------

message_of_the_day (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

