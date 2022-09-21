.. _cp_gaia_put_file_module:


cp_gaia_put_file -- Add a new file to a Check Point machine.
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add a new file to a Check Point machine.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  file_name (True, str, None)
    Filename include the desired path. The file will be created in the user home directory if the full path wasn't provided.


  text_content (True, str, None)
    Content to add to the new file.


  override (False, bool, False)
    If the file already exists, indicates whether to overwrite it. Recommended value is true. Note When the value is false, if the file already exists in the system from an previous execution, it will fail.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add a file
      check_point.gaia.cp_gaia_put_file:
        file_name: "ansible_file.txt"
        text_content: "It's an ansible file."
        override: true




Return Values
-------------

put_file (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Yuval Feiger (@chkp-yuvalfe)

