.. _cp_gaia_password_policy_module:


cp_gaia_password_policy -- Setting password policy configuration.
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Setting password policy configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- supported starting from gaia_api >= 1.6



Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  lock_settings (False, dict, None)
    Password change configuration.


    inactivity_settings (False, dict, None)
      Inactivity configuration.


      lock_unused_accounts_enabled (False, bool, False)
        Password lock unused accounts.


      inactivity_threshold_days (False, int, 365)
        Inactivity days to password expiration lockout, Valid values are 1-1827.



    failed_attempts_settings (False, dict, None)
      Failed attempts configuration.


      failed_lock_duration_seconds (False, int, 1200)
        Password failed logging lockout duration, Valid values are 60-604800.


      failed_lock_enforced_on_admin (False, bool, False)
        Enforce failed lockout on admin user.


      failed_lock_enabled (False, bool, False)
        Lock user after exceeded maximum allowed login attempts.


      failed_attempts_allowed (False, int, 10)
        Amount of login attempts allowed before lockout, Valid values are 2-1000.



    password_expiration_days (False, int, None)
      Password expiration lifetime, Valid values are 60-604800.


    password_expiration_warning_days (False, int, 7)
      Number of days before a password expires that the user gets warned, Valid values are 1-366.


    password_expiration_maximum_days_before_lock (False, int, None)
      Password expiration lockout in days, Valid values are 1-1827.


    must_one_time_password_enabled (False, bool, False)
      Forces a user to change their password after it has been set via "User Management" (but not via "Self Password Change" or forced change at login). Use this command to set the value.



  password_history (False, dict, None)
    Password history configuration.


    check_history_enabled (False, bool, False)
      Password history check.


    repeated_history_length (False, int, 10)
      Password history length.



  password_strength (False, dict, None)
    Password history configuration.


    minimum_length (False, int, 6)
      Password minimum length, Valid values are 6-128.


    complexity (False, int, 2)
      Password complexity, Valid values are 1-4.


    palindrome_check_enabled (False, bool, True)
      Password palindrome check.






Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change password policy
      check_point.gaia.cp_gaia_password_policy:
            lock_settings: {'failed_attempts_settings': {'failed_attempts_allowed': 10,
                                                         'failed_lock_duration_seconds': 1200,
                                                         'failed_lock_enabled': False,
                                                         'failed_lock_enforced_on_admin': False},
                            'inactivity_settings': {'inactivity_threshold_days': 365, 'lock_unused_accounts_enabled': False},
                            'must_one_time_password_enabled': False,
                            'password_expiration_days': 60,
                            'password_expiration_maximum_days_before_lock': 1000,
                            'password_expiration_warning_days': 7}
            password_history: {'check_history_enabled': True, 'repeated_history_length': 10}
            password_strength: {'complexity': 2, 'minimum_length': 6, 'palindrome_check_enabled': True}



Return Values
-------------

password_policy (always., dict, )
  The checkpoint object updated.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

