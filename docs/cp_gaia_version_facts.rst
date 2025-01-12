.. _cp_gaia_version_facts_module:


cp_gaia_version_facts -- Show gaia version.
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show gaia version.



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

    
    - name: Show version
      check_point.gaia.cp_gaia_version_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The version facts.


  product_version (always, str, )
    Gaia version.


  os_build (always, str, )
    Build number.


  os_kernel_version (always, str, )
    Gaia kernel version.


  os_edition (always, str, )
    Gaia edition.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

