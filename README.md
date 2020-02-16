# Check Point Ansible Gaia Collection
This Ansible collection provides control over a Check Point machine using
Check Point's web-services APIs.

This is the repository of the gaia collection which can be found here - https://galaxy.ansible.com/check_point/gaia

Installation instructions
-------------------------
Run `ansible-galaxy collection install check_point.gaia`

Requirements
------------
* Ansible 2.9+ is required.
* The Check Point server should have Gaia API engine installed on.

Usage
-----
1. Edit the `hosts` so that it will contain a section similar to this one:
```
[check_point]
%CHECK_POINT_MANAGEMENT_SERVER_IP%
[check_point:vars]
ansible_httpapi_use_ssl=True
ansible_httpapi_validate_certs=False
ansible_user=%CHECK_POINT_GAIA_USER%
ansible_password=%CHECK_POINT_GAIA_PASSWORD%
ansible_network_os=check_point.gaia.checkpoint
```
<br><br>2. Run a playbook:
```sh
ansible-playbook your_ansible_playbook.yml
```

Example playbook:
```
---
- name: playbook name
  hosts: check_point
  connection: httpapi
  tasks:
    - name: task to have network
      check_point.mgmt.cp_gaia_hostname:
        name: "newhost"
```
Modules
-------
* `cp_gaia_hostname` – Manage the hostname of a Check Point machine over Web Services API.
* `cp_gaia_hostname_facts` – Get the hostname of a Check Point machine over Web Services API.
* `cp_gaia_physical_interface` – Manage physical interface of a Check Point machine over Web Services API.
* `cp_gaia_physical_interfaces_facts` – Get information about physical interfaces of a Check Point machine over Web Services API.
* `cp_gaia_put_file` – Add a new file to a Check Point machine over Web Services API.
