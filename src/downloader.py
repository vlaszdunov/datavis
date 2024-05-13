import requests
from urllib.parse import urlencode
import os

class Downloader:

    api_url = "https://cloud-api.yandex.net/v1/disk/public/resources?"

    @staticmethod
    def __init__(CLOUD_URL):
        if os.path.exists('Downloaded')==False:
            os.mkdir('Downloaded')

        request_url = Downloader.api_url + urlencode(dict(public_key=CLOUD_URL))
        response=requests.get(request_url).json()['_embedded']['items']
        for file in response:
            if file['name']=='Список общий.xlsx':
                downloaded=requests.get(response[response.index(file)]['file']).content
                break

        open('Downloaded/students_info.xlsx', 'wb').write(downloaded)

    def delete_downloaded():
        os.remove('Downloaded/students_info.xlsx')
        os.rmdir('Downloaded')
