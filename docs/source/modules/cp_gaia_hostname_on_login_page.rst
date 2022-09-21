.. _cp_gaia_hostname_on_login_page_module:


cp_gaia_hostname_on_login_page -- Enable/disable the hostname on login page message.
====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting the hostname on login page message.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  enabled (False, bool, False)
    Hostname on WebUI login page enabled.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - hostname_on_login_page: Changing the banner message
      check_point.gaia.cp_gaia_hostname_on_login_page:
        enabled: True




Return Values
-------------

hostname_on_login_page (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

