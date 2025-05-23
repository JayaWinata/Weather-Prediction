from src import logger
from src.pipeline.data_ingestion import DataIngestionPipeline
from src.pipeline.data_transformation import DataTransformationPipeline
from src.pipeline.model_trainer import ModelTrainerPipeline
from src.pipeline.model_evaluation import ModelEvaluationPipeline

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

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
    obj = ModelTrainerPipeline()
    obj.train_model()
    logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
    obj = ModelEvaluationPipeline()
    obj.evaluate()
    logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
except Exception as e:
    logger.exception(e)
    raise e