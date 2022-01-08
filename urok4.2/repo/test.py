#!/usr/bin/env python3
import json
import socket
host = {'drive.google.com': '',
        'mail.google.com': '',
        'google.com': ''
        }
for name in host:
    host[f'{name}'] = socket.gethostbyname(f'{name}')
    #print (host)
    print(f'{name} '+host[f'{name}'])
out_file = open('json_out','w+')
json.dump(host,out_file)
#sleep(3)  # Задержка перед следующим сравнением

