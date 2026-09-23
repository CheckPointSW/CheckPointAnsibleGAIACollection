# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2018 Red Hat Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import time
from ansible.module_utils.connection import Connection

BEFORE_REQUEST = 1
AFTER_REQUEST = 2

checkpoint_argument_spec_for_async = dict(
    wait_for_task=dict(type='bool', default=True)
)

checkpoint_argument_spec_for_async_false = dict(
    wait_for_task=dict(type='bool', default=False)
)

checkpoint_argument_spec_for_all = dict(
    version=dict(type='str'),
    virtual_system_id=dict(type="int", required=False)
)


# parse failure message with code and response
def parse_fail_message(code, response):
    if isinstance(response, dict):
        msg = response.get('message', str(response))
    else:
        msg = str(response)
    if code == 404:
        msg += ' (verify the API endpoint is supported on your Gaia API version)'
    return 'Checkpoint device returned error {0} with message {1}'.format(code, msg)


def _task_error_detail(task):
    details = task.get('task-details') or []
    detail = details[0] if details else {}
    return detail.get('error') or detail.get('output') or ''


def _fail_task(module, task, reason='failed', detail=''):
    if not detail:
        detail = _task_error_detail(task) or 'Look at the logs for more details'
    module.fail_json(msg='Task {0} with task id {1} {2}: {3}'.format(
        task.get('task-name', ''), task.get('task-id', ''), reason, detail)
    )


def _check_task_success(module, task):
    details = task.get('task-details') or []
    rc = details[0].get('return-value') if details else None
    if rc is not None and rc != 0:
        error_msg = _task_error_detail(task) or 'Look at the logs for more details'
        _fail_task(module, task, 'completed with error', error_msg)


def idempotency_check(old_val, new_val):
    if isinstance(new_val, dict):
        for key in new_val:
            if key in old_val:
                if idempotency_check(old_val[key], new_val[key]) is False:
                    return False
    elif isinstance(new_val, list):
        if len(new_val) != len(old_val):
            return False
        for new_item in new_val:
            if not any(idempotency_check(old_item, new_item) for old_item in old_val):
                return False
    else:
        if str(new_val) != str(old_val):
            return False
    return True


# if user insert a specific version, we add it to the url
def get_version(module):
    if module.params.get('version'):
        res = ('v' + module.params['version'] + '/')
        del module.params['version']
    else:
        res = ''
    return res


# send the request to checkpoint
def send_request(connection, version, url, payload=None):
    code, response = connection.send_request('/gaia_api/' + version + url, payload)
    return code, response


# get the payload from the user parameters
def is_checkpoint_param(parameter):
    if parameter == 'state' or \
            parameter == 'wait_for_task':
        return False
    return True


# build the payload from the parameters which has value (not None), and they are parameter of checkpoint API as well
def replace_chkp_params(params, request_type):
    params = dict(params)  # avoid mutating the caller's dict
    payload = {}
    old = ""
    new = ""
    if request_type == BEFORE_REQUEST:
        old = "_"
        new = "-"
        # we used a dedicated 'msg' parametr because we can not use 'message' parameter
        # as 'message' is used internally in Ansible Core engine
        if "msg" in params:
            params["message"] = params.pop("msg")
        if "ver" in params:
            params["version"] = params.pop("ver")
    elif request_type == AFTER_REQUEST:
        old = "-"
        new = "_"
        if "message" in params:
            params["msg"] = params.pop("message")
        if "version" in params:
            params["ver"] = params.pop("version")

    for parameter in params:
        parameter_value = params[parameter]
        if parameter_value is not None and is_checkpoint_param(parameter):
            if isinstance(parameter_value, dict):
                payload[parameter.replace(old, new)] = replace_chkp_params(parameter_value, request_type)
            elif isinstance(parameter_value, list) and len(parameter_value) != 0 and isinstance(parameter_value[0], dict):
                payload_list = []
                for element_dict in parameter_value:
                    payload_list.append(replace_chkp_params(element_dict, request_type))
                payload[parameter.replace(old, new)] = payload_list
            else:
                payload[parameter.replace(old, new)] = parameter_value
    return payload


# wait for task
def wait_for_task(module, version, task_id):
    task_id_payload = {'task-id': task_id}
    task_complete = False
    current_iteration = 0
    max_num_iterations = 300

    connection = Connection(module._socket_path)
    # As long as there is a task in progress
    while not task_complete and current_iteration < max_num_iterations:
        current_iteration += 1
        # Check the status of the task
        code, response = send_request(connection, version, 'show-task', task_id_payload)
        # reboot flow
        attempts_counter = 0
        while code != 200:
            if attempts_counter < 40:
                attempts_counter += 1
                time.sleep(3)
                code, response = send_request(connection, version, 'show-task', task_id_payload)
            else:
                res = "ERROR: Failed to handle asynchronous tasks as synchronous, tasks result is undefined. "
                module.fail_json(msg=parse_fail_message(code, res))

        # Count the number of tasks that are not in-progress
        completed_tasks = 0
        for task in response['tasks']:
            status = task.get('status')
            if status == 'failed':
                _fail_task(module, task)
            if status == 'in progress':
                break
            completed_tasks += 1
            if status == 'succeeded':
                _check_task_success(module, task)

        # Are we done? check if all tasks are completed
        if completed_tasks == len(response["tasks"]):
            task_complete = True
        else:
            time.sleep(2)  # Wait for two seconds
    if not task_complete:
        module.fail_json(msg="ERROR: Timeout. Task-id: {0}.".format(task_id_payload['task-id']))

    return response


# handle api call
def api_call(module, target_version, api_call_object):
    payload = replace_chkp_params(module.params, BEFORE_REQUEST)
    connection = Connection(module._socket_path)
    code, response = send_request(connection, target_version, api_call_object, payload)

    response = replace_chkp_params(response, AFTER_REQUEST)
    return code, response


def chkp_facts_api_call(module, api_call_object, is_multible):
    target_version = get_version(module)
    if is_multible is True:
        show_single = False
        module_key_params = dict((k, v) for k, v in module.params.items() if v is not None)
        if "static-route" == api_call_object:
            if "address" in module_key_params and "mask_length" in module_key_params:
                show_single = True
        elif "maestro" in api_call_object:
            if "id" in module_key_params or "interface_name" in module_key_params or "site_id" in module_key_params:
                show_single = True
        else:
            if len(module_key_params) > 0:
                show_single = True

        if show_single is True:
            code, res = api_call(module, target_version, api_call_object="show-{0}".format(api_call_object))
        else:
            code, res = api_call(module, target_version, api_call_object="show-{0}s".format(api_call_object))
    else:
        code, res = api_call(module, target_version, api_call_object="show-{0}".format(api_call_object))

    if code != 200:
        module.fail_json(msg=parse_fail_message(code, res))

    return {
        "ansible_facts": res
    }


def _strip_ignore(d, ignore):
    def _filter(val):
        if isinstance(val, dict):
            return {k: _filter(v) for k, v in val.items() if k not in ignore}
        elif isinstance(val, list):
            return [_filter(v) for v in val]
        return val
    return _filter(d)


# drop the suboptions the user did not set, at every level, so they don't show up as a change
def _strip_unset(val):
    if isinstance(val, dict):
        return {k: _strip_unset(v) for k, v in val.items() if v is not None}
    elif isinstance(val, list):
        return [_strip_unset(v) for v in val]
    return val


# the parameters the user asked for, without the ones that are not part of the object itself
def _desired_params(module, ignore):
    desired = dict((k, v) for k, v in module.params.items()
                   if is_checkpoint_param(k) and v is not None and k not in checkpoint_argument_spec_for_all)
    return _strip_ignore(_strip_unset(desired), ignore)


# merge the desired parameters onto the current state, to preview what a set/add call would produce
def _preview_after(before, desired):
    after = dict(before)
    for key, value in desired.items():
        if isinstance(value, dict) and isinstance(after.get(key), dict):
            after[key] = _preview_after(after[key], value)
        elif key in after and idempotency_check(after[key], value) is True:
            # already at the requested value, keep the current one so the diff stays clean
            continue
        else:
            after[key] = value
    return after


# build the result of a change that check mode stopped us from making
def _check_mode_result(api_call_object, before, after, with_diff=True):
    result = {
        api_call_object.replace('-', '_'): after,
        "changed": True
    }
    if with_diff:
        result['diff'] = {'before': before, 'after': after}
    return result


def chkp_api_call(module, api_call_object, has_add_api, ignore=None, show_params=None, add_params=None, is_maestro_special=False, compare_params=None):
    target_version = get_version(module)
    changed = False
    if show_params is None:
        show_params = []
    if ignore is None:
        ignore = []
    modules_params_original = module.params
    module_params_show = dict((k, v) for k, v in module.params.items() if k in show_params and v is not None)
    module.params = module_params_show
    if not is_maestro_special:
        code, res = api_call(module, target_version, api_call_object="show-{0}".format(api_call_object))
        res = _strip_ignore(res, ignore)
        before = res.copy()
    else:
        code, res = api_call(module, target_version, api_call_object="show-maestro-security-groups")
        res = _strip_ignore(res, ignore)
        before = res.copy()

    # Run the command:
    module.params = modules_params_original
    if 'state' in module.params and module.params['state'] == 'absent':  # handle delete
        if is_maestro_special:
            # pending changes would be discarded, the resulting state can not be previewed
            if module.check_mode:
                return _check_mode_result(api_call_object, before, before, with_diff=False)
            code, res = api_call(module, target_version, api_call_object="discard-{0}".format(api_call_object))
        else:
            if code == 200:
                # the object exists, so it would be deleted
                if module.check_mode:
                    return _check_mode_result(api_call_object, before, {})
                # delete/show require same params
                module.params = module_params_show
                code, res = api_call(module, target_version, api_call_object="delete-{0}".format(api_call_object))
            else:
                return {
                    api_call_object.replace('-', '_'): {},
                    'diff': {'before': {}, 'after': {}},
                    "changed": False
                }
    else:  # handle set/add
        if is_maestro_special:
            # pending changes would be applied, the resulting state can not be previewed
            if module.check_mode:
                return _check_mode_result(api_call_object, before, before, with_diff=False)
            code, res = api_call(module, target_version, api_call_object="apply-{0}".format(api_call_object))
        else:
            params_dict = dict((k, v) for k, v in module.params.items() if is_checkpoint_param(k) and v is not None)

            if code == 200:
                params_for_idempotency = compare_params if compare_params is not None else params_dict
                if idempotency_check(res, params_for_idempotency) is True:
                    return {
                        api_call_object.replace('-', '_'): res,
                        'diff': {'before': res, 'after': res},
                        "changed": False
                    }
                # the object exists but differs from the requested state, so it would be modified
                if module.check_mode:
                    return _check_mode_result(api_call_object, before, _preview_after(before, _desired_params(module, ignore)))
                code, res = api_call(module, target_version, api_call_object="set-{0}".format(api_call_object))
            else:
                # the object does not exist yet, so it would be created
                if module.check_mode:
                    return _check_mode_result(api_call_object, {}, _desired_params(module, ignore))
                if has_add_api is True:
                    if add_params:
                        [module.params.pop(key) for key in show_params if key not in add_params]
                        module.params.update(add_params)
                        if 'loopback-interface' == api_call_object:  # loopback doesn't take 'name' for add-... api
                            if 'name' in module.params:
                                module.params.pop("name")
                    code, res = api_call(module, target_version, api_call_object="add-{0}".format(api_call_object))
                else:  # some requests like static-route don't have add, try set instead
                    code, res = api_call(module, target_version, api_call_object="set-{0}".format(api_call_object))

    if code == 200:
        if 'wait_for_task' in module.params and module.params['wait_for_task'] is True:
            if 'task_id' in res:
                res = wait_for_task(module, target_version, res['task_id'])
    else:
        module.fail_json(msg=parse_fail_message(code, res))

    after = _strip_ignore(res, ignore)
    changed = False if before == after else True

    return {
        api_call_object.replace('-', '_'): res,
        'diff': {'before': before, 'after': after},
        "changed": changed
    }


# for operation and async tasks
def chkp_api_operation(module, api_call_object, read_only=False):
    target_version = get_version(module)
    # 'show-...' operations don't modify the device, so they must still run under check mode
    read_only = read_only or api_call_object.startswith('show-')
    # these operations are imperative, there is no state to diff, so we can only report that
    # the module would have run
    if module.check_mode and not read_only:
        return {'changed': True}
    code, response = api_call(module, target_version, api_call_object)
    result = {'changed': True}
    if code == 200:
        if 'wait_for_task' in module.params and module.params['wait_for_task'] is True:
            if 'task_id' in response:
                response = wait_for_task(module, target_version, response['task_id'])

        result[api_call_object.replace('-', '_')] = response
    else:
        module.fail_json(msg=parse_fail_message(code, response))

    return result
