import src.downloader as downloader
from src.parse import Parser
from src.visualiser import create_heatmap
from src.settings import Settings

config = Settings()
file = downloader.get_file(
    config.cloud_url, config.cloud_filename)
parsed_data=Parser(file)
create_heatmap(parsed_data.study_group_1)
