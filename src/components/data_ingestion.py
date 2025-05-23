from src.entity.config_entity import DataIngestionConfig
from src.constants import *
from src import logger
import pandas as pd

from urllib.parse import urlencode
import urllib.request as request
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.data_path):
            # Build URL
            params = urlencode(self.config.url_params, doseq=True)
            url = f"{self.config.base_source_url}?{params}"
            print(url)

            # Download file
            filename, headers = request.urlretrieve(
                url=url,
                filename=self.config.data_path
            )
            logger.info(f'{filename} downloaded! Info:\n{headers}')
        else:
            logger.info("File already exists")

        try:
            df = pd.read_csv(self.config.data_path)
        except Exception as e:
            logger.error(e)
            df = pd.read_csv(self.config.data_path, skiprows=3)
        df.columns = df.columns.str.replace(r"\s*\(.*?\)", "", regex=True)
        df.columns = df.columns.str.strip()
        df.to_csv(self.config.data_path, index=False)

        logger.info("Column names renamed and file saved.")

    def get_daily_data(self):
        pass