#!/usr/bin/python

# Copyright: (c) 2023, Petr Losev <wowpetr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file
short_description: Creates text files with custom content
version_added: "1.0.0"
description: Creates text files with custom content on node.
options:
  path:
    description: Path to the file being created.
    required: true
    type: path
  content:
    description: Content of the file.
    required: false
    type: str
author:
    - Petr Losev (@wowpetr)
'''

EXAMPLES = r'''
- name: Create ~/example.txt file
  wowpetr.netology.create_file:
    path: ~/example.txt
    content: Created with ansible module wowpetr.netology.create_file

- name: Create an empty file
  wowpetr.netology.create_file:
    path: /tmp/empty_file"
'''

RETURN = r'''
path:
  description: Path to created file or directory.
  returned: success
  type: str
  sample: /path/to/file.txt
'''

import os
from traceback import format_exc

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native


def create_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


def file_already_exists(path, content):
    if os.path.exists(path):
        current_content = ""
        with open(path, "r") as f:
            current_content = f.read()
        return current_content == content


def main():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result = dict(
        changed=False,
        path=path
    )

    if not file_already_exists(path, content):
        if module.check_mode:
            result['changed'] = True
        else:
            try:
                create_file(path, content)
                result['changed'] = True
            except Exception as e:
                module.fail_json(msg=to_native(e), exception=format_exc())

    module.exit_json(**result)


if __name__ == '__main__':
    main()
