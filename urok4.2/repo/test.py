#!/usr/bin/env python3
import os
import requests
gd = 'drive.google.com'
gm = 'mail.google.com'
gg = 'google.com'
r = requests.get(f'http://{gm}')
#print(type(r))
if r.status_code == 200:
    bash_command = [f'ping /n 4 {gm}']
    result_os = os.popen(' && '.join(bash_command)).read()
    print(result_os)
    for result in result_os.split('\n'):
        if result.find(f'{gg}') != -1:
            print(result)
            #prepare_result = result.replace('Pinging ', '' '')
            array=result.split(" ")
            print(array[1:3])
