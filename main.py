from cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifier import logger

Stage_Name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    ingestion = DataIngestionPipeline()
    ingestion.star_data_ingestion()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e
    