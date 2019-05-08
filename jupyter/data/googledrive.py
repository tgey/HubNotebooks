import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.client import GoogleCredentials


def download_data_from_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile(
        {'q': "'17YUaUJdFzgUVEQ5rhk01Xgqo2l68rhON' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
        file_id = file1['id']
        downloaded = drive.CreateFile({'id': file_id})
        downloaded.GetContentFile(file1['title'])
        os.rename(file1['title'], 'raw/eip/' + file1['title'])

if __name__ == '__main__':
    download_data_from_drive()
