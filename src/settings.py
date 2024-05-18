import os
import dotenv


class Settings:
    '''
    Configure program with data from `.env` file
    
    Attributes:
        cloud_url (str): Link to a public folder in the cloud
        cloud_filename (str): name of the file to be downloaded from the cloud
    '''
    
    cloud_url: str
    cloud_filename: str

    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.cloud_url = os.getenv('CLOUD_URL')  # type: ignore
        self.cloud_filename = os.getenv('CLOUD_FILENAME')  # type: ignore
