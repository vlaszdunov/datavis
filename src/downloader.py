import requests
from urllib.parse import urlencode
import os

class Downloader:

    cloud_url='https://disk.yandex.ru/d/x9IYS-jGXcpyqw'
    api_url = "https://cloud-api.yandex.net/v1/disk/public/resources?"
    request_url = api_url + urlencode(dict(public_key=cloud_url))

    @staticmethod
    def __init__():
        if os.path.exists('Downloaded')==False:
            os.mkdir('Downloaded')

        response=requests.get(Downloader.request_url).json()['_embedded']['items']
        for file in response:
            if file['name']=='Список общий.xlsx':
                downloaded=requests.get(response[response.index(file)]['file']).content
                break

        open('Downloaded/students_info.xlsx', 'wb').write(downloaded)

    def delete_downloaded():
        os.remove('Downloaded/students_info.xlsx')
        os.rmdir('Downloaded')
