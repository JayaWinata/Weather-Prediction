from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def train_model(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(f'>>>>>  {STAGE_NAME} started  <<<<<')
        obj = ModelTrainerPipeline()
        obj.train_model()
        logger.info(f'>>>>>  {STAGE_NAME} finished  <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e