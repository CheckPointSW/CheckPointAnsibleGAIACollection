.. _cp_gaia_dns_facts_module:


cp_gaia_dns_facts -- Show DNS settings.
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show DNS settings.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show current dns configuration
      check_point.gaia.cp_gaia_dns_facts:





Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  suffix (always., str, )
    Use empty-string in order to remove the setting.


  primary (always., str, )
    Use empty-string in order to remove the setting.


  tertiary (always., str, )
    Use empty-string in order to remove the setting.


  secondary (always., str, )
    Use empty-string in order to remove the setting.






Status
------





Authors
~~~~~~~

- Majd Sharkia (@chkp-majds)

