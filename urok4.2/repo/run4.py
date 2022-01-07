#!/usr/bin/env python3
import os
import requests
gd = 'drive.google.com'
gm = 'mail.google.com'
gg = 'google.com'
r = requests.get(f'http://{gg}')
if r == 200:
    bash_command = [f"ping /n 4 {gg}"]
    result_os = os.popen(' && '.join(bash_command)).read()
    #is_change = True
    for result in result_os.split('\n'):
        if result.find('Ответ от') != -1:
            prepare_result = result.replace()
        print(f'{prepare_result}')