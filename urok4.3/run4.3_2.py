#!/usr/bin/env python3
import json
import socket
import yaml
with open('json_out.json') as json_file:
    host = json.load(json_file)
    #print(host)
for name in host:
    ip = host[f'{name}']
    #print (ip)
    if ip == socket.gethostbyname(f'{name}'):
        print (f'{name} ' + socket.gethostbyname(f'{name}'))
    else:
        print(f'{name} ' + f'Старый ip - {ip}' + ', новый ip - ' + socket.gethostbyname(f'{name}'))
        #print(host)
        print('Изменяем ip на новый')
        host[f'{name}'] = socket.gethostbyname(f'{name}')
out_file = open('json_out.json', 'w+')
json.dump(host, out_file, indent=2)
print('Записываен новые данные в json файл')
out_file2 = open('yaml_out.yaml', 'w+')
yaml.dump(host, out_file2, indent=2, explicit_start=True, explicit_end=True)
print('Записываен новые данные в yaml файл')