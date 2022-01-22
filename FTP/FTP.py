from ftplib import FTP
import json
from _datetime import datetime
import os

'''Сохраняем время запуска в Date_now'''
Date_now = datetime.now()
'''Проверяем наличие в текущем каталоге временной папки и если такой нет - создаем'''
try:
    os.mkdir('Temp')
except FileExistsError:
    pass
'''Проверяем наличие файлов во временной папке, если есть - удаляем'''
for path, dirs, files in os.walk('Temp'):
    for file in files:
        os.unlink(os.path.join(path, file))
'''Загружаем в словарь конфиг из джсончика'''
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


ftp = FTP('ftp.zakupki.gov.ru')
ftp.login('free', 'free')
ftp.close()
