.. _cp_gaia_grub_password_facts_module:


cp_gaia_grub_password_facts -- Show GRUB hash password.
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show the GRUB hash password.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.7



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.7.


  virtual_system_id (False, int, None)
    Virtual System ID.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show GRUB hash password
      check_point.gaia.cp_gaia_grub_password_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  password_hash (always, str, )
    An encrypted representation of the password.






Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

