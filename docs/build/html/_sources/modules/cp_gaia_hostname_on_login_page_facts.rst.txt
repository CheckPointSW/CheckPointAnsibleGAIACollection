.. _cp_gaia_hostname_on_login_page_facts_module:


cp_gaia_hostname_on_login_page_facts -- Show hostname_on_login_page message settings.
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show Hostname on login page message settings.



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

    
    - name: Show hostname_on_login_page message settings
      check_point.gaia.cp_gaia_hostname_on_login_page_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  enabled (always, bool, )
    Hostname on Gaia Portal login page enabled (true/false).






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

