import requests

API_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources?'


def get_file(CLOUD_URL: str, CLOUD_FILENAME: str) -> bytes:

    download_link = get_download_link(CLOUD_URL, CLOUD_FILENAME)

    file_content = requests.get(download_link).content
    return file_content


def get_download_link(CLOUD_URL: str, CLOUD_FILENAME: str) -> str:
    params: dict['str', 'str'] = {'public_key': CLOUD_URL,
                                  'path': f'/{CLOUD_FILENAME}',
                                  'fields': 'file'}
    response: dict[str, str] = requests.get(API_URL, params).json()

    try:
        return response['file']
    except KeyError:
        print('Файл или папка отсутствуют в Я.Диске.\nПроверьте правильность URL папки и названия файла в .env')
        exit()
