import os
import dotenv

class Settings:

    cloud_url=''

    def __init__(self) -> None:
        dotenv.load_dotenv() 
        self.cloud_url=os.getenv('CLOUD_URL')