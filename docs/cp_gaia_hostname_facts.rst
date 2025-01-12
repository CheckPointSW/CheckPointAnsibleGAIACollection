.. _cp_gaia_hostname_facts_module:


cp_gaia_hostname_facts -- Show hostname settings.
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show hostname settings.






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

    
    - name: Show current hostname
      check_point.gaia.cp_gaia_hostname_facts:




Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  name (always, str, )
    Hostname.






Status
------





Authors
~~~~~~~

- Yuval Feiger (@chkp-yuvalfe)

