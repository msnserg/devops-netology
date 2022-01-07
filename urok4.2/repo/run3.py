#!/usr/bin/env python3

import os
command= input('Введите полный путь к дериктории\n')
path1 = 'C:/Users/admin/Documents/GitHub/devops-netology'
if command == path1:
   bash_command = [(f"cd {path1}"), "git status"]
   result_os = os.popen(' && '.join(bash_command)).read()
   #is_change = True
   for result in result_os.split('\n'):
       if result.find('modified') != -1:
           prepare_result = result.replace('\tmodified:   ', '')
           print(f'{path1}/{prepare_result}')
else:
    print("Указанный путь не является репозиторием Git!\n ")