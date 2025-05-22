from src.utils.helper import read_yaml, create_directories
from src.entity.config_entity import (DataIngestionConfig, DataTransformationConfig)
from src.constants import *

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILEPATH,
                 params_filepath = PARAMS_FILEPATH,
                 schema_filepath = SCHEMA_FILEPATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            base_source_url = config.base_source_url,
            data_path= config.data_path,
            url_params = config.url_params,
            target_dir = config.target_dir
        )

        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            transformed_filename = config.transformed_filename
        )

        return data_transformation_config
