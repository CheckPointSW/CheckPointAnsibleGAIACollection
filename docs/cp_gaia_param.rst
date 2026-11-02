.. _cp_gaia_param_module:


cp_gaia_param -- Set Config Point parameters.
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Config Point parameters.

To see the parameters documentation go to https://\<IP\>/param\_docs/ on the Gaia machine.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia\_api \>= 1.8
- supported on Gaia versions R82 and above



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.8.


  virtual_system_id (False, str, None)
    VSX Virtual System ID which presents the context switch.


  param_list (True, list, None)
    List of parameters to be set.


    param_path (True, str, None)
      Parameter full path.


    value (optional, raw, None)
      Parameter value, can be a string, int, boolean, object or a list of them.

      Can not be used together with :emphasis:`use\_default`.


    comments (optional, str, None)
      Comments to be added to the parameter, length is limited to 256 characters.


    use_default (optional, bool, None)
      Set the parameter back to its default value.

      Can not be used together with :emphasis:`value`.


    volatile (optional, bool, None)
      Set the parameter with the value specified until the next reboot.


    virtual_system_id (optional, str, None)
      VSX Virtual System IDs to set the parameter in, can be :literal:`all` or specific IDs, for example :literal:`2,4,7\-10`.



  dry_run (False, bool, False)
    Run the request without saving to the database, return only the values that would change.


  use_regex (False, bool, False)
    Indicates that :emphasis:`param\_path` includes :literal:`\*`.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`. In check mode the request is sent with :literal:`dry\_run`\ , so nothing is saved.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set a parameter value and return another one to its default
      check_point.gaia.cp_gaia_param:
        param_list:
          - param_path: gaia.infra.httpd.cp_httpd_configuration.children_core_dumps
            value: true
            comments: enabled for debugging purpose
          - param_path: gaia.infra.rest_api.gunicorn.timeout
            use_default: true

    - name: Check which parameters would change, without saving
      check_point.gaia.cp_gaia_param:
        param_list:
          - param_path: gaia.infra.httpd.cp_httpd_configuration.children_core_dumps
            value: true
        dry_run: true



Return Values
-------------

set_param (always., dict, )
  The task result of the set\-param request, including the parameters that were set.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

