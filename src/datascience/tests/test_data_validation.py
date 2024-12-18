import pytest
from src.datascience.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.datascience.utils.common import read_yaml
from src.datascience.components.data_validation import DataValiadtion
from src.datascience.entity.config_entity import (
    DataValidationConfig
)


@pytest.fixture
def data_validation_config():
    configs = read_yaml(CONFIG_FILE_PATH)
    config = configs.data_validation
    schemas = read_yaml(SCHEMA_FILE_PATH)
    schema = schemas.COLUMNS
    return DataValidationConfig(
        root_dir=config.root_dir,
        STATUS_FILE=config.STATUS_FILE,
        unzip_data_dir=config.unzip_data_dir,
        all_schema=schema,
    )


def test_validate_all_columns(data_validation_config):
    validation = DataValiadtion(config=data_validation_config)
    validation_status = validation.validate_all_columns()
    assert validation_status is True
