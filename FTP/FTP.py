from ftplib import FTP
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

ftp = FTP('ftp.zakupki.gov.ru')
ftp.login('free', 'free')
ftp.close()
