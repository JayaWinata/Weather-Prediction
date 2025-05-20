from src import logger
from src.pipeline.data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
    obj = DataIngestionPipeline()
    obj.ingest_data()
    logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
except Exception as e:
    logger.exception(e)
    raise e