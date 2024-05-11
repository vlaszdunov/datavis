import requests
from urllib.parse import urlencode
import os

class Downloader:

    url='https://disk.yandex.ru/d/x9IYS-jGXcpyqw'
    api_url = "https://cloud-api.yandex.net/v1/disk/public/resources?"
    request_url = api_url + urlencode(dict(public_key=url))

    @staticmethod
    def __init__() -> None:
        if os.path.exists('Downloaded')==False:
            os.mkdir('Downloaded')

        response=requests.get(Downloader.request_url).json()['_embedded']['items']
        for file in response:
            if file['name']=='Список общий.xlsx':
                downloaded=requests.get(response[response.index(file)]['file']).content

        open('Downloaded/students_info.xlsx', 'wb').write(downloaded)

Downloader()