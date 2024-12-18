import os
import pytest

from src.datascience.constants import CONFIG_FILE_PATH
from src.datascience.utils.common import read_yaml
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.entity.config_entity import (
    DataTransformationConfig
)


@pytest.fixture
def data_transformation_config():
    configs = read_yaml(CONFIG_FILE_PATH)
    config = configs.data_transformation
    return DataTransformationConfig(
        root_dir=config.root_dir,
        data_path=config.data_path,
    )


def test_train_test_splitting(data_transformation_config):
    transformation = DataTransformation(config=data_transformation_config)
    transformation.train_test_splitting()
    assert os.path.exists("artifacts/data_transformation/train.csv")
    assert os.path.exists("artifacts/data_transformation/test.csv")
