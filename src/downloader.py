import requests
import os

API_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources?'


def get_file(CLOUD_URL: str | None, CLOUD_FILENAME: str | None) -> bytes:
    '''
    Load data from requested file

    Args:
        CLOUD_URL (str): Link to a public folder in the cloud
        CLOUD_FILENAME (str): name of the file to be downloaded from the cloud

    Returns:
        bytes: byte content of the file
    '''

    download_link = get_download_link(CLOUD_URL, CLOUD_FILENAME)

    file_content = requests.get(download_link).content
    return file_content


def get_download_link(CLOUD_URL: str | None, CLOUD_FILENAME: str | None) -> str:
    '''
    Sends a request to Yandex.Disk and returns a link
    to download the file from the cloud

    Args:
        CLOUD_URL (str): Link to a public folder in the cloud
        CLOUD_FILENAME (str): name of the file to be downloaded from the cloud

    Returns:
        str: download link for specified file
    '''

    params: dict[str, str | None] = {'public_key': CLOUD_URL,
                                     'path': f'/{CLOUD_FILENAME}',
                                     'fields': 'file'}
    """Additional params for HTTPS request"""

    response: dict[str, str] = requests.get(API_URL, params).json()
    """Data received from the server upon request"""

    try:
        return response['file']
    except KeyError:
        print('Файл или папка отсутствуют в Я.Диске.\n\
            Проверьте правильность URL папки и названия файла в .env')
        exit()
    finally:
        del os.environ['CLOUD_URL']
        del os.environ['CLOUD_FILENAME']
