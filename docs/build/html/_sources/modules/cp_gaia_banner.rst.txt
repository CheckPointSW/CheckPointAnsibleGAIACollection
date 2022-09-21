.. _cp_gaia_banner_module:


cp_gaia_banner -- Setting the banner message.
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting the banner message.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  msg (False, str, This system is for authorized use only.)
    Banner message for the web, ssh and serial login. Empty string returns to default.


  enabled (False, bool, None)
    Banner message enabled.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - banner: Changing the banner message
      check_point.gaia.cp_gaia_banner:
        msg: new_message




Return Values
-------------

banner (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

