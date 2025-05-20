from src.entity.config_entity import DataIngestionConfig
from src.constants import *
from src import logger

from urllib.parse import urlencode
import urllib.request as request
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.data_path):
            params = urlencode(self.config.url_params, doseq=True)
            url = f"{self.config.base_source_url}?{params}"
            print(url)
            filename, headers = request.urlretrieve(
                url = url,
                filename = self.config.data_path
            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info("File already exists")

    def get_daily_data(self):
        pass