from ftplib import FTP
from datetime import datetime
import os

# Текущая дата (для едедневной папки)
current_path = str(datetime.now().date().strftime('%Y%m%d'))


def make_dir(current_path):
    try:
        os.mkdir(current_path)
    except FileExistsError:
        pass

ftp = FTP('ftp.zakupki.gov.ru')
ftp.login('free', 'free')
ftp.cwd('fcs_regions/Tulskaja_obl/contracts/currMonth')
filenames = ftp.nlst()
print(os.getcwd())
print(filenames)
make_dir(current_path)
ftp.quit()
