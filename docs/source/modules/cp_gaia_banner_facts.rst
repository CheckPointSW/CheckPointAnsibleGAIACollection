.. _cp_gaia_banner_facts_module:


cp_gaia_banner_facts -- Show banner message settings.
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show banner message.



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

    
    - name: Show banner message
      check_point.gaia.cp_gaia_banner_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  message (always, str, )
    Banner message.


  enabled (always, bool, )
    If banner enabled.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

