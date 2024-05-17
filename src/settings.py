import os
import dotenv


class Settings:

    cloud_url: str
    cloud_filename: str

    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.cloud_url = os.getenv('CLOUD_URL')
        self.cloud_filename = os.getenv('CLOUD_FILENAME')