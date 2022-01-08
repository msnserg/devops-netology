#!/usr/bin/env python3
import json
import socket
with open('json_out') as json_file:
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
out_file = open('json_out', 'w+')
json.dump(host, out_file)
print('Записываен новые данные')