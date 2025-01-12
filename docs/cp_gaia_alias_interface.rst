.. _cp_gaia_alias_interface_module:


cp_gaia_alias_interface -- Modify alias interface.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify alias interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (True, str, None)
    Interface name with format "\<parent interface\>:\<id\>", for example  eth0:1, eth0:2 .. etc.


  ipv4_address (False, str, None)
    Interface IPv4 address.


  ipv4_mask_length (False, int, None)
    Interface IPv4 address mask length.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set comment field of a alias interface
      check_point.gaia.cp_gaia_alias_interface:
        comments: "eth0:1 interface"
        name: eth0:1



Return Values
-------------

alias_interface (always., dict, )
  The updated interface details.





Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

