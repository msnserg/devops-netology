#Домашнее задание к занятию  
##"4.3. Языки разметки JSON и YAML"
###Задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису: 
```json


{ "info" : "Sample JSON output from our service\\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : "7175" 
        },
        { "name" : "second",
        "type" : "proxy",
        "ip" : "71.78.22.43"
        }
    ]
}
```
Нужно найти и исправить все ошибки, которые допускает наш сервис

###Задача 2  
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.  

Создадим промежуточный файл
```python
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
out_file = open('json_out.json','w+')
json.dump(host,out_file)                               
```
Далее работаем с ним  
```python
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
```

Дополнительное задание (со звездочкой*) - необязательно к выполнению
Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:

Принимать на вход имя файла
Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов