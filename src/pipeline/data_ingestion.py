from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def ingest_data(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
        obj = DataIngestionPipeline()
        obj.ingest_data()
        logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e