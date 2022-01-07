#!/usr/bin/env python3

import os
bash_command = ["cd  C:/Users/admin/Documents/GitHub/devops-netology", "git status"]
path1 = 'C:/Users/admin/Documents/GitHub/devops-netology'
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = True
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f'{path1}/{prepare_result}')
