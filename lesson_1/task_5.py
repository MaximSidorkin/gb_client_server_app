'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
'''

import subprocess

try:
    print('\n START YANDEX PING\n')
    args = ['ping', 'yandex.ru', '-c 5']
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
except:
    print('неизвестная ошибка!')

try:
    print('\n START YOUTOBE PING\n')
    args = ['ping', 'youtube.com', '-c 5']
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
except:
    print('неизвестная ошибка!')