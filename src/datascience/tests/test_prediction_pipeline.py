import os
import pytest
import pandas as pd


def test_prediction_pipeline():
    from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

    # Features expected by the model
    feature_columns = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
    ]

    # Sample input aligned with the features
    sample_data = pd.DataFrame([{
        "fixed acidity": 7.4,
        "volatile acidity": 0.7,
        "citric acid": 0.0,
        "residual sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur dioxide": 11.0,
        "total sulfur dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
    }])

    pipeline = PredictionPipeline()
    prediction = pipeline.predict(sample_data)

    # Assert prediction length
    assert len(prediction) == 1
