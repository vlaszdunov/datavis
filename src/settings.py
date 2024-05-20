import os

import dotenv


def load_config() -> dict[str, str | None]:
    '''
    Configure program with data from `.env` file

    Return:
        config (dict[str,str]). Dict with cloud_url
        and cloud_filename environmnet variables
        Keys: CLOUD_URL: url to cloud folder
              CLOUD_FILENAME: name of the file on the cloud
    '''
    dotenv.load_dotenv()
    config = {'CLOUD_URL': os.getenv('CLOUD_URL'),
              'CLOUD_FILENAME': os.getenv('CLOUD_FILENAME')}
    return config
