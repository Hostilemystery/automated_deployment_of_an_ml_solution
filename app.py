from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info(
    "app_info", "App Info, this can be anything you want", version="1.0.0")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                             chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                             pH, sulphates, alcohol]).reshape(1, -1)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            return jsonify({"prediction": predict[0]})
        except Exception as e:
            print(f"Exception: {e}")
            return jsonify({"error": "Invalid input or prediction error."})
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def train():
    os.system("python main.py")
    return jsonify({"message": "Model training successful!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
