import os
import pytest
from src.datascience.constants import CONFIG_FILE_PATH
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.utils.common import read_yaml
from src.datascience.entity.config_entity import (
    DataIngestionConfig
)


# Data Ingestion Test
@pytest.fixture
def data_ingestion_config():
    configs = read_yaml(CONFIG_FILE_PATH)
    config = configs.data_ingestion
    return DataIngestionConfig(
        root_dir=config.root_dir,
        source_URL=config.source_URL,
        local_data_file=config.local_data_file,
        unzip_dir=config.unzip_dir
    )


def test_download_file(data_ingestion_config):
    ingestion = DataIngestion(config=data_ingestion_config)
    ingestion.download_file()
    assert os.path.exists(data_ingestion_config.local_data_file)


def test_extract_zip_file(data_ingestion_config):
    ingestion = DataIngestion(config=data_ingestion_config)
    ingestion.extract_zip_file()
    assert os.path.exists(data_ingestion_config.unzip_dir)
