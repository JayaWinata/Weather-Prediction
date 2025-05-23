from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src import logger

STAGE_NAME = "Model Training Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def evaluate(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
        obj = ModelEvaluationPipeline()
        obj.evaluate()
        logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e