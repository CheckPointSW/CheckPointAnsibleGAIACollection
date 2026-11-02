.. _cp_gaia_param_facts_module:


cp_gaia_param_facts -- Show Config Point parameters.
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show Config Point parameters by full path or prefix.

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


  param_path (True, str, None)
    Parameter full path or prefix, for example :literal:`security\-gateway.DLP`.


  filter_by (False, str, None)
    Show only parameters matching the filter, in the format :literal:`\<filter\_type\>=true`.

    The filter type can be one of :literal:`modified`\ , :literal:`with\-comments` or :literal:`not\-default`\ , for example :literal:`modified=true`.


  member_id (False, int, None)
    SMO member ID of the member to show the data from. Default is the ID of the current login member.


  wait_for_task (False, bool, True)
    Wait for task or return immediately.





Notes
-----

.. note::
   - Supports :literal:`check\_mode`.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show all DLP parameters
      check_point.gaia.cp_gaia_param_facts:
        param_path: security-gateway.DLP

    - name: Show only the DLP parameters that were modified
      check_point.gaia.cp_gaia_param_facts:
        param_path: security-gateway.DLP
        filter_by: modified=true



Return Values
-------------

show_param (always., dict, )
  The task result of the show\-param request.

  The matching parameters are in :literal:`tasks[0].task\-details[0].param\-list`\ , each with its name, current\-value, default\-value, description, comments, pending and last\-modified.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

