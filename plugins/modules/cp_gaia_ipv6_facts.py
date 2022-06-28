#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = """
author: Majd Sharkia (@chkp-majds)
description:
- Check IPv6 support in the machine's operating system
module: cp_gaia_ipv6_facts
short_description: Check IPv6 support in the machine's operating system
version_added: '2.0.0'
requirements:
- supported starting from gaia_api >= 1.6


"""


EXAMPLES = """
- name: Show IPv6 status
  cp_gaia_ipv6_facts:


"""


RETURN = """
ansible_facts:
  description: The checkpoint object facts.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_facts_api_call


def main():
    # arguments for the module:
    fields = dict(

    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ipv6'
    gaia_api_version = 'v1.6/'

    res = chkp_facts_api_call(module, gaia_api_version, api_call_object, False)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
