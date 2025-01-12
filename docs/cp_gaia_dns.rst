.. _cp_gaia_dns_module:


cp_gaia_dns -- Setting DNS configuration.
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting DNS configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  suffix (False, str, None)
    Use empty-string in order to remove the setting.


  primary (False, str, None)
    Use empty-string in order to remove the setting.


  tertiary (False, str, None)
    Use empty-string in order to remove the setting.


  secondary (False, str, None)
    Use empty-string in order to remove the setting.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Setting dns servers for the system
      check_point.gaia.cp_gaia_dns:
        suffix: "checkpoint.com"
        primary: "1.2.3.4"
        tertiary: "3.4.5.6"
        secondary: "2.3.4.5"




Return Values
-------------

dns (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

