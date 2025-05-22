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
        data.dropna(subset=['weather_code'], inplace=True)
        data.to_csv(os.path.join(self.config.root_dir, self.config.transformed_filename), index=False)

        logger.info("Missing value handled successfully")

    def train_test_spliting(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, self.config.transformed_filename))

        train, test = train_test_split(data, test_size=.25)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")