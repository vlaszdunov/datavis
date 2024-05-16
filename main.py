import src.downloader as downloader
from src.parse import Parser
from src.visualiser import Visualiser
from src.settings import Settings

config = Settings()
visual=Visualiser()
file = downloader.get_file(
    config.cloud_url, config.cloud_filename)
visual.heatmap(Parser(file).study_group_1)
