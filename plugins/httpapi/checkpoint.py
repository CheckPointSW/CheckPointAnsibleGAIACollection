# (c) 2018 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = """
---
author: Ansible Networking Team (@ansible-network)
name : checkpoint
short_description: HttpApi Plugin for Checkpoint devices
description:
  - This HttpApi plugin provides methods to connect to Checkpoint
    devices over a HTTP(S)-based api.
version_added: "2.8.0"
options:
  cptarget:
    type: str
    description:
      - target gateway
    vars:
      - name: ansible_checkpoint_target
  domain:
    type: str
    description:
      - Specifies the domain of the Check Point device
    vars:
      - name: ansible_checkpoint_domain
  api_key:
    type: str
    description:
      - Login with api-key instead of user & password
    vars:
      - name: ansible_api_key
  cloud_mgmt_id:
    type: str
    description:
      - The Cloud Management ID
    vars:
      - name: ansible_cloud_mgmt_id
"""

import json

from ansible.module_utils.basic import to_text
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.plugins.httpapi import HttpApiBase
from ansible.module_utils.connection import ConnectionError
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

BASE_HEADERS = {
    'Content-Type': 'application/json',
    'cp-gaia-orchestrator': 'Ansible'
}


class HttpApi(HttpApiBase):
    def __init__(self, connection):
        super(HttpApi, self).__init__(connection)
        self.connection = connection
        self.mgmt_proxy_enabled = False
        
        loader = DataLoader()
        # Initialize InventoryManager
        inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
        # Get host
        host = inventory.get_host('mgmt_proxy')
        # Get variable
        try:
            proxy_enabled = host.vars['enabled']
            if proxy_enabled == True:
                self.mgmt_proxy_enabled = True
        except Exception as e:
            pass


    def login(self, username, password):
        payload = {}
        url = '/gaia_api/login'
        cp_domain = self.get_option('domain')
        cp_api_key = self.get_option('api_key')
        if cp_domain:
            payload['domain'] = cp_domain
        if username and password and not cp_api_key:
            payload['user'] = username
            payload['password'] = password
        elif cp_api_key and not username and not password:
            payload['api-key'] = cp_api_key
        else:
            raise AnsibleConnectionFailure('[Username and password] or api_key are required for login')
        if self.mgmt_proxy_enabled == True:
            url = '/web_api/login'
        response, response_data = self.send_request(url, payload)

        try:
            self.connection._auth = {'X-chkp-sid': response_data['sid']}
        except KeyError:
            raise ConnectionError(
                'Server returned response without token info during connection authentication: %s' % response_data)
        # Case of read-only
        if 'uid' in response_data.keys():
            self.connection._session_uid = response_data['uid']

    def logout(self):
        url = '/gaia_api/logout'
        if self.mgmt_proxy_enabled == True:
            url = '/web_api/logout'
        response, dummy = self.send_request(url, None)

    def get_session_uid(self):
        return self.connection._session_uid

    def send_request(self, path, body_params):
        cp_cloud_mgmt_id = self.get_option('cloud_mgmt_id')
        if cp_cloud_mgmt_id:
            path = '/' + cp_cloud_mgmt_id + path
        # we only replace gaia_ip/ with web_api/gaia-api/ if target is set and path contails for gaia_ip/
        cp_api_target = self.get_option('cptarget')
        if 'gaia_api/' in path: # Avoid login/logut requests in case of web_api
            if self.mgmt_proxy_enabled == True:
                if cp_api_target != None:
                    body_params['target'] = cp_api_target
                path = path.replace("gaia_api/", "web_api/gaia-api/")
        data = json.dumps(body_params) if body_params else '{}'

        try:
            self._display_request()
            response, response_data = self.connection.send(path, data, method='POST', headers=BASE_HEADERS)
            value = self._get_response_value(response_data)

            return response.getcode(), self._response_to_json(value)
        except AnsibleConnectionFailure as e:
            return 404, e.message
        except HTTPError as e:
            error = json.loads(e.read())
            return e.code, error

    def _display_request(self):
        self.connection.queue_message('vvvv', 'Web Services: %s %s' % ('POST', self.connection._url))

    def _get_response_value(self, response_data):
        return to_text(response_data.getvalue())

    def _response_to_json(self, response_text):
        try:
            return json.loads(response_text) if response_text else {}
        # JSONDecodeError only available on Python 3.5+
        except ValueError:
            raise ConnectionError('Invalid JSON response: %s' % response_text)
