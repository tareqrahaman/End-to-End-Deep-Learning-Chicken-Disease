from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import Evaluation


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run_evaluation_pipeline(self):
        try:
            config_manager = ConfigurationManager()
            eval_config = config_manager.get_evaluation_config()
            evaluation = Evaluation(config=eval_config)
            evaluation.evaluation()
            evaluation.save_score()
        except Exception as e:
            raise e