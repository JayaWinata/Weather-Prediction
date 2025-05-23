from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def transform_data(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.handle_missing_values()
        data_transformation.feature_engineering()
        data_transformation.train_test_spliting()

if __name__ == "__main__":
    try:
        logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
        obj = DataTransformationPipeline()
        obj.transform_data()
        logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e