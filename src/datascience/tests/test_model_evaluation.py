import os
import pytest
import pandas as pd
import joblib
from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience.utils.common import read_yaml
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.entity.config_entity import (
    ModelEvaluationConfig,
)


@pytest.fixture
def model_evaluation_config():
    configs = read_yaml(CONFIG_FILE_PATH)
    config = configs.model_evaluation
    schemas = read_yaml(SCHEMA_FILE_PATH)
    schema = schemas.TARGET_COLUMN
    param = read_yaml(PARAMS_FILE_PATH)
    params = param.ElasticNet
    return ModelEvaluationConfig(
        root_dir=config.root_dir,
        test_data_path=config.test_data_path,
        model_path=config.model_path,
        all_params=params,
        metric_file_name=config.metric_file_name,
        target_column=schema.name,
        mlflow_uri="https://dagshub.com/Hostilemystery/automated_deployment_of_an_ml_solution.mlflow"
    )


def test_eval_metrics(model_evaluation_config):
    evaluation = ModelEvaluation(config=model_evaluation_config)
    test_data = pd.read_csv(model_evaluation_config.test_data_path)
    model = joblib.load(model_evaluation_config.model_path)
    test_x = test_data.drop([model_evaluation_config.target_column], axis=1)
    test_y = test_data[[model_evaluation_config.target_column]]

    predicted_qualities = model.predict(test_x)
    rmse, mae, r2 = evaluation.eval_metrics(test_y, predicted_qualities)

    assert rmse >= 0
    assert mae >= 0
    assert -1 <= r2 <= 1


def test_log_into_mlflow(model_evaluation_config):
    evaluation = ModelEvaluation(config=model_evaluation_config)
    evaluation.log_into_mlflow()
    assert os.path.exists(model_evaluation_config.metric_file_name)
