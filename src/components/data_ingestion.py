from src.entity.config_entity import DataIngestionConfig
from src.constants import *
from src import logger
import pandas as pd

from datetime import datetime, timedelta
from urllib.parse import urlencode
import urllib.request as request
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        params = urlencode(self.config.url_params, doseq=True)
        url = f"{self.config.base_source_url}?{params}&start_date={datetime.today().date() - timedelta(days=90)}&end_date={datetime.today().date()}"
        if not os.path.exists(self.config.data_path):
            print(url)
            filename, headers = request.urlretrieve(
                url = url,
                filename = self.config.data_path
            )
            logger.info(f'{filename} download! with following info: \n{headers}')

            df = pd.read_csv(self.config.data_path, skiprows=3)
            df.columns = df.columns.str.replace(r'\s*\(.*?\)', '', regex=True)
            df.to_csv(self.config.data_path, index=False)
        else:
            logger.info("File already exists, appending data....")
            self.__append_data(url)

    def get_daily_data(self):
        pass

    def __append_data(self, url):
        filename, headers = request.urlretrieve(
            url = url,
            filename = f'{self.config.root_dir}/temp.csv'
        )
        logger.info(f'{filename} download! with following info: \n{headers}')
        df = pd.read_csv(self.config.data_path)
        temp = pd.read_csv(f'{self.config.root_dir}/temp.csv', skiprows=3)
        temp.columns = temp.columns.str.replace(r'\s*\(.*?\)', '', regex=True)

        final = pd.concat([df, temp], ignore_index=True)
        final.to_csv(self.config.data_path, index=False)

        if os.path.exists(f'{self.config.root_dir}/temp.csv'):
            os.remove(f'{self.config.root_dir}/temp.csv')