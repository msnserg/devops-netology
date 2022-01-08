##Задание4  
Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.  

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
out_file = open('json_out','w+')                              
json.dump(host,out_file)                                      
```
Далее работаем с ним  
```python
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
```