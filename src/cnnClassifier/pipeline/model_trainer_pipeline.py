from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Model_Trainer
from cnnClassifier import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def start_model_trainer_pipeline(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_model_trainer_config()
            training = Model_Trainer(training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
            logger.info("Model training is completed.")
        except Exception as e:
            raise e