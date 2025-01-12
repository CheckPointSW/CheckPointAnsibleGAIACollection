.. _cp_gaia_asset_facts_module:


cp_gaia_asset_facts -- Show Asset.
==================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show Asset.



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

    
    - name: Show Asset
      check_point.gaia.cp_gaia_asset_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The asset facts.


  ac (always, list, )
    The AC asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  disk (always, list, )
    The disk asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  lom_info (always, list, )
    The lom asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  memory (always, list, )
    The memory asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  network (always, list, )
    The network asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  power_supply (always, list, )
    The power supply asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  sam (always, list, )
    The sam asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.



  system (always, list, )
    The system asset.


    key (, str, )
      The asset element key.


    value (, str, )
      The asset element value.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

