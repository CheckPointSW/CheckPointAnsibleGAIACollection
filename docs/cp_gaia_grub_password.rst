.. _cp_gaia_grub_password_module:


cp_gaia_grub_password -- Sets GRUB password.
============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Sets GRUB password.



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


  password (False, str, None)
    GRUB new password.


  password_hash (False, str, None)
    An encrypted representation of the password.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Setting GRUB new password
      check_point.gaia.cp_gaia_grub_password:
        password: newpass



Return Values
-------------

grub_password (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

