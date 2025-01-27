.. _cp_gaia_loopback_interface_module:


cp_gaia_loopback_interface -- Modify loopback interface.
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify loopback interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  virtual_system_id (False, int, None)
    Virtual System ID.


  state (False, str, present)
    Ansible state which can be \ :literal:`present`\  or \ :literal:`absent`\ .


  name (False, str, None)
    Interface name with format \ :literal:`loop\<id\>`\ , for example "loop00", "loop01"

    Not required when adding new loopback interface

    Newly-created loopback interface name returned in dict details


  ipv4_address (False, str, None)
    Interface IPv4 address.


  ipv4_mask_length (False, int, None)
    Interface IPv4 address mask length.


  ipv6_address (False, str, None)
    Interface IPv6 address.


  ipv6_autoconfig (False, bool, None)
    Configure IPv6 auto-configuration.


  ipv6_mask_length (False, int, None)
    Interface IPv6 address mask length.


  comments (False, str, None)
    Interface Comments.


  enabled (False, bool, None)
    Interface State.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set comment field of a loopback interface
      check_point.gaia.cp_gaia_loopback_interface:
        comments: "loop01 interface"
        name: loop01




Return Values
-------------

loopback_interface (always., dict, )
  The updated interface details.





Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

