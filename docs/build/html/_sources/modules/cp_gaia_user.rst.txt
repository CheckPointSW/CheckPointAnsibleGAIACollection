.. _cp_gaia_user_module:


cp_gaia_user -- Change a user's characteristics.
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change a user's characteristics.






Parameters
----------

  version (False, str, None)
    Gaia API version for example 1.6.


  state (False, str, present)
    Ansible state which can be ``present`` or ``absent``.


  name (True, str, None)
    User name.


  shell (False, str, cli)
    Specifies the user's default command line interpreter during login.


  homedir (False, str, None)
    Specifies the user's home directory as the full UNIX path name where the user is placed on login. If the directory doesn't exist, it is created. Range  Must be under '/home' and must not contain colon. Unless set, the default 'homedir' will be '/home/user-name'.


  secondary_system_groups (False, list, None)
    This operation sets the groups of the user. Valid values must be names of known groups.


  password_hash (False, str, None)
    An encrypted representation of the password. Hash version of a password can be generated using the 'grub-md5-crypt' utility.


  must_change_password (False, bool, None)
    Forcing password change is relevant only when a password is set. When set to 'True' Force the user to change their password the next time they log in. If they don't log in within the time limit configured in 'set password-controls expiration-lockout-days' they may not be able to log in at all. When set to 'False' If the user was being forced to change their password, cancel that. If the user was locked out due to failure to change their password within the time limit configured in 'set password-controls expiration-lockout-days' they will no longer be locked out.


  real_name (False, str, None)
    Specifies a string describing a user; conventionally it's the user's full name. Default is Username, capitalized.


  unlock (False, bool, None)
    If the user has been locked out, cancel that. True cancel lock-out. False  do nothing.


  allow_access_using (False, list, ['CLI', 'Web-UI'])
    Modify the access-mechanisms available for a user. Valid values are ``CLI`` ``Web-UI`` ``Gaia-API`` (supported from R81.10).


  roles (False, list, None)
    Roles spesified to the user.


  primary_system_group_id (False, int, 100)
    GID. Numeric ID which is used in identifying the primary group to which this user belongs.


  password (False, str, None)
    Specifies new password on command line. Check Point recommends that a password be at least eight characters long. A password must contain at least six characters. Enforcement level can be modified via 'password control' feature.


  uid (False, int, None)
    Specifies a numeric user ID used to identify permissions of a user, duplicate UIDs are not allowed.





Notes
-----

.. note::
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set shell field for the user
      check_point.gaia.cp_gaia_user:
        shell: bash
        name: admin




Return Values
-------------

user (always., dict, )
  The updated user details.





Status
------





Authors
~~~~~~~

- Ameer Asli (@chkp-ameera)

