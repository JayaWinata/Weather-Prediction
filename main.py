from src import logger
from src.pipeline.data_ingestion import DataIngestionPipeline
from src.pipeline.data_transformation import DataTransformationPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
    obj = DataIngestionPipeline()
    obj.ingest_data()
    logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
    obj = DataTransformationPipeline()
    obj.transform_data()
    logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
except Exception as e:
    logger.exception(e)
    raise e