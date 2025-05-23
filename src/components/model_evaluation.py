import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from urllib.parse import urlparse
import mlflow
import numpy as np
import joblib
import dagshub
from src.entity.config_entity import ModelEvaluationConfig
from src.utils.helper import save_json
from pathlib import Path

dagshub.init(repo_owner='jayawinata100', repo_name='Weather-Prediction', mlflow=True)

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, predicted):
        accuracy = accuracy_score(actual, predicted)
        precision = precision_score(actual, predicted, average='weighted')
        recall = recall_score(actual, predicted, average='weighted')
        f1 = f1_score(actual, predicted, average='weighted')
        return accuracy, precision, recall, f1

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_value = model.predict(test_x)
            accuracy, precision, recall, f1 = self.eval_metrics(test_y, predicted_value)

            score = {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1_score': f1}
            save_json(path=Path(self.config.metric_file_name), data=score)

            mlflow.log_params(self.config.model_params)

            mlflow.log_metric("accuracy", accuracy)
            # mlflow.log_text(str(classification_report(test_y, predicted_value)))

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="RFClassifierModel")
            else:
                mlflow.sklearn.log_model(model, "model")