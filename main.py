import src.downloader as downloader
from src.dataparser import *
from src.visualiser import create_heatmap
from src.settings import load_config

config = load_config()
file = downloader.get_file(
    config['CLOUD_URL'], config['CLOUD_FILENAME'])
parsed_data = create_list_of_groups(file)
create_heatmap(parsed_data)