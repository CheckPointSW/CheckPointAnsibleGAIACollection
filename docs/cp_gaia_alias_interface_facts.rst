.. _cp_gaia_alias_interface_facts_module:


cp_gaia_alias_interface_facts -- Show alias interface/s.
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show alias interface.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (False, str, None)
    Interface name to show. If not specified, all alias interfaces information is returned.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show alias interface
      check_point.gaia.cp_gaia_alias_interface_facts:
    - name: Show alias interface by specifying it's name
      check_point.gaia.cp_gaia_alias_interface_facts:
        name: eth0:1



Return Values
-------------

ansible_facts (always., dict, )
  The interface/s facts.


  objects (always, list, )
    List of interfaces.


    name (always, str, )
      Interface name.


    ipv4_address (always, str, )
      Interface IPv4 address.


    ipv4_mask_length (always, int, )
      Interface IPv4 address mask length.


    enabled (always, bool, )
      Interface State.







Status
------





Authors
~~~~~~~

- Duane Toler (@duanetoler)

