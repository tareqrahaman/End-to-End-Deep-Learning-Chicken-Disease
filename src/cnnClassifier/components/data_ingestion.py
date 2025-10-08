import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Download file from Google Drive"""
        if not os.path.exists(self.config.local_data_file):
            gdown.download(
                self.config.source_URL,
                str(self.config.local_data_file),
                quiet=False
            )
            logger.info(f"File downloaded: {self.config.local_data_file}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")
    
    def extract_zip_file(self):
        """Extract the zip file into the data directory"""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted to: {unzip_path}")