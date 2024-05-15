from urllib.parse import urlencode
import time

import requests

API_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources?'
CLOUD_URL = 'https://disk.yandex.ru/d/x9IYS-jGXcpyqw'

request_url = API_URL + \
    urlencode({'public_key': CLOUD_URL})
a = requests.get(request_url, params={
                 'path': '/Список общий.xlsx', 'fields': 'file'})
print(time.process_time())

print(a.iter_content(decode_unicode=True))
