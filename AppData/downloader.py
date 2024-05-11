import requests
from urllib.parse import urlencode
url='https://disk.yandex.ru/d/x9IYS-jGXcpyqw'
resources = "https://cloud-api.yandex.net/v1/disk/public/resources?"
requests_url = resources + urlencode(dict(public_key=url))

response=requests.get(requests_url).json()['_embedded']['items'][7]
print(response['file'])
print('')
downloaded=requests.get(response['file'])
with open('Downloaded/students_info.xlsx', 'wb') as ff:
    ff.write(downloaded.content)