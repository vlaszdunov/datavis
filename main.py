import src.downloader as downloader
from src.dataparser import *
from src.visualiser import create_heatmap
from src.settings import Settings
import time

config = Settings()
file = downloader.get_file(
    config.cloud_url, config.cloud_filename)
parsed_data = create_list_of_groups(file)
create_heatmap(parsed_data)
print(time.process_time())