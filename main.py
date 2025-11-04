from cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifier.pipeline.preapre_base_model_pipeline import PrepareBaseModelPipeline
from cnnClassifier.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from cnnClassifier.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from cnnClassifier import logger

Stage_Name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    ingestion = DataIngestionPipeline()
    ingestion.start_data_ingestion()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

Stage_Name = "Prepare Base Model"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    model = PrepareBaseModelPipeline()
    model.start_prepare_base_model()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

Stage_Name = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    train = ModelTrainerPipeline()
    train.start_model_trainer_pipeline()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

Stage_Name = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    evaluate = ModelEvaluationPipeline()
    evaluate.run_evaluation_pipeline()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e