from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    def start_data_ingestion(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)

            data_ingestion.download_file()
            logger.info("Download completed.")

            data_ingestion.extract_zip_file()
            logger.info("Extraction completed.")
        except Exception as e:
            raise e