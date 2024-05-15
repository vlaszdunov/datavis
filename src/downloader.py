import os
from urllib.parse import urlencode

import requests

API_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources?'
DOWNLOAD_DIR_NAME = 'downloaded'
DOWNLOADED_FILE_NAME = 'students_info.xlsx'


def download_file(CLOUD_URL: str, CLOUD_FILENAME: str) -> None:
    if os.path.exists(DOWNLOAD_DIR_NAME) == False:
        os.mkdir(DOWNLOAD_DIR_NAME)

    download_link = get_download_link(CLOUD_URL, CLOUD_FILENAME)
    if download_link is None:
        print(f'Файл {CLOUD_FILENAME} отсутствует в облаке')
        exit()

    try:
        file_content = requests.get(download_link).content
    except requests.exceptions.MissingSchema:
        print('ошибка')
        exit()
    else:
        open(f'{DOWNLOAD_DIR_NAME}/{DOWNLOADED_FILE_NAME}',
             'wb').write(file_content)


def get_download_link(CLOUD_URL, CLOUD_FILENAME) -> str:
    param = urlencode({'public_key': CLOUD_URL,
                      'path': f'/{CLOUD_FILENAME}',
                      'fields': 'file'})
    response: dict[str, str] = requests.get(API_URL, params=param).json()
    return response['file']


def delete_downloaded():
    os.remove(f'{DOWNLOAD_DIR_NAME}/{DOWNLOADED_FILE_NAME}')
    os.rmdir(f'{DOWNLOAD_DIR_NAME}')
