from src.downloader import Downloader
from src.pars import Parse
from src.heatmap import Heatmap
from src.settings import Settings

config=Settings()
Downloader(config.cloud_url)
Parse()
Downloader.delete_downloaded()
Heatmap(Parse.study_group_1)