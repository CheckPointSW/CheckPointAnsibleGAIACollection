.. _cp_gaia_hostname_module:


cp_gaia_hostname -- Setting the hostname of a machine.
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting the hostname of a machine.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  name (True, str, None)
    New hostname to change. Hostname can be a combination of letters and numbers, it cannot be in IP format or start/end with characters such as ''.'' And ''-''.





Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Changing a hostname
      check_point.gaia.cp_gaia_hostname:
        name: new-hostname




Return Values
-------------

hostname (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Yuval Feiger (@chkp-yuvalfe)

