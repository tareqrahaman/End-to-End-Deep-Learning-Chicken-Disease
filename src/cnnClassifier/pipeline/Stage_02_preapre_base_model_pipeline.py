from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def start_prepare_base_model(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
            prepare_base_model.get_base_model()
            logger.info("Base model is prepared and saved.")
            prepare_base_model.upadate_base_model()
            logger.info("Updated Base model is ready and saved.")
        except Exception as e:
            raise e