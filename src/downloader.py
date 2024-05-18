import requests
import os

API_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources?'


def get_file(cloud_url: str, cloud_filename: str) -> bytes:
    '''
    Load data from requested file
    
    Args:
        cloud_url (str): Link to a public folder in the cloud
        cloud_filename (str): name of the file to be downloaded from the cloud
    
    Returns:
        bytes: byte content of the file
    '''

    download_link = get_download_link(cloud_url, cloud_filename)

    file_content = requests.get(download_link).content
    return file_content


def get_download_link(cloud_url: str, cloud_filename: str) -> str:  
    '''
    Sends a request to Yandex.Disk and returns a link
    to download the file from the cloud

    Args:
        cloud_url (str): Link to a public folder in the cloud
        cloud_filename (str): name of the file to be downloaded from the cloud

    Returns:
        str: download link for specified file
    '''
 
    params: dict['str', 'str'] = {'public_key': cloud_url,
                                  'path': f'/{cloud_filename}',
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
        del os.environ['cloud_url']
        del os.environ['cloud_filename']
