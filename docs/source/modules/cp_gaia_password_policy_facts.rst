.. _cp_gaia_password_policy_facts_module:


cp_gaia_password_policy_facts -- Show password policy configuration.
====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show password policy configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show password policy configuration
      check_point.gaia.cp_gaia_password_policy_facts:



Return Values
-------------

ansible_facts (always., dict, )
  The checkpoint object facts.


  lock_settings (always, dict, )
    Password change configuration.


    inactivity_settings (always, dict, )
      Inactivity configuration.


      lock_unused_accounts_enabled (always, bool, )
        Password lock unused accounts.


      inactivity_threshold_days (always, int, )
        Inactivity days to password expiration lockout, Valid values are 1-1827.



    failed_attempts_settings (always, dict, )
      Failed attempts configuration.


      failed_lock_duration_seconds (always, int, )
        Password failed logging lockout duration, Valid values are 60-604800.


      failed_lock_enforced_on_admin (always, bool, )
        Enforce failed lockout on admin user.


      failed_lock_enabled (always, bool, )
        Lock user after exceeded maximum allowed login attempts.


      failed_attempts_allowed (always, int, )
        Amount of login attempts allowed before lockout, Valid values are 2-1000.



    password_expiration_days (always, int, )
      Password expiration lifetime, Valid values are 60-604800.


    password_expiration_warning_days (always, int, )
      Number of days before a password expires that the user gets warned, Valid values are 1-366.


    password_expiration_maximum_days_before_lock (always, int, )
      Password expiration lockout in days, Valid values are 1-1827.


    must_one_time_password_enabled (always, bool, )
      Forces a user to change their password after it has been set via "User Management" (but not via "Self Password Change" or forced change at login). Use this command to set the value.



  password_history (always, dict, )
    Password history configuration.


    check_history_enabled (always, bool, )
      Password history check.


    repeated_history_length (always, int, )
      Password history length.



  password_strength (always, dict, )
    Password history configuration.


    minimum_length (always, int, )
      Password minimum length, Valid values are 6-128.


    complexity (always, int, )
      Password complexity, Valid values are 1-4.


    palindrome_check_enabled (always, bool, )
      Password palindrome check.







Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

