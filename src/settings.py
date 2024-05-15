import os
import dotenv


class Settings:

    cloud_url = ''
    cloud_filename = ''

    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.cloud_url = os.getenv('CLOUD_URL')
        self.cloud_filename = os.getenv('CLOUD_FILENAME')
        if self.cloud_url is None:
            print('В файле конфигурации отсутсвует ссылка на паку в облаке')
            exit()
        if self.cloud_filename is None:
            print('В файле конфигурации отсутсвует название файла в папке на диске')
            exit()
