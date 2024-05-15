from src.downloader import delete_downloaded, download_file
from src.heatmap import heatmap
from src.pars import Parse
from src.settings import Settings
import time
import os

config = Settings()
download_file(config.cloud_url, config.cloud_filename)
Parse()
delete_downloaded()
heatmap(Parse.study_group_1)