from src.downloader import Downloader
from src.pars import Parse
from src.heatmap import Heatmap

# Heatmap(Parse.study_group_1)

Downloader()
Parse()
Downloader.delete_downloaded()
Heatmap(Parse.study_group_1)