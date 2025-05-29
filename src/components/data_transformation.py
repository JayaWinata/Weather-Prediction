import os
from src import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def handle_missing_values(self):
        data = pd.read_csv(self.config.data_path)
        logger.info(f"Null values:\n{data.isna().sum()}")
        data.dropna(how='any', inplace=True)
        data.to_csv(os.path.join(self.config.root_dir, self.config.transformed_filename), index=False)

        logger.info(f"Null values:\n{data.isna().sum()}")
        logger.info("Missing value handled successfully")

    def remove_duplicates(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, self.config.transformed_filename))
        data.drop_duplicates()
        data.to_csv(os.path.join(self.config.root_dir, self.config.transformed_filename), index=False)

        logger.info('Duplicated data removed successfully')

    def feature_engineering(self):
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm: slight or moderate",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }

        data = pd.read_csv(os.path.join(self.config.root_dir, self.config.transformed_filename))
        data['weather'] = data['weather_code'].apply(lambda x: weather_codes.get(x, "Unknown"))
        data.drop(['weather_code', 'time'], axis=1, inplace=True)
        data.to_csv(os.path.join(self.config.root_dir, self.config.transformed_filename), index=False)

        logger.info('Feature engineering done successfully')

    def train_test_spliting(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, self.config.transformed_filename))

        train, test = train_test_split(data, test_size=.25)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")