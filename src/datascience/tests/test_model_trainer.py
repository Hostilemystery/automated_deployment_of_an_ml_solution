import os
import pytest
from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience.utils.common import read_yaml
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.entity.config_entity import (
    ModelTrainerConfig
)


@pytest.fixture
def model_trainer_config():
    configs = read_yaml(CONFIG_FILE_PATH)
    config = configs.model_trainer
    schemas = read_yaml(SCHEMA_FILE_PATH)
    schema = schemas.TARGET_COLUMN
    param = read_yaml(PARAMS_FILE_PATH)
    params = param.ElasticNet
    return ModelTrainerConfig(
        root_dir=config.root_dir,
        train_data_path=config.train_data_path,
        test_data_path=config.test_data_path,
        model_name=config.model_name,
        alpha=params.alpha,
        l1_ratio=params.l1_ratio,
        target_column=schema.name
    )


def test_train_model(model_trainer_config):
    trainer = ModelTrainer(config=model_trainer_config)
    trainer.train()
    assert os.path.exists("artifacts/model_trainer/model.joblib")
