from frameworks.shared.utils import Timer
from frameworks.shared.callee import call_run, result

from interpret.glassbox import ExplainableBoostingRegressor, ExplainableBoostingClassifier
import pandas as pd

def run(dataset, config):
    cls = ExplainableBoostingRegressor if config.type == 'regression' else ExplainableBoostingClassifier
    learner = cls()

    with Timer() as training:
        train_data = pd.read_parquet(dataset.train)
        X, y = train_data.loc[:, train_data.columns != dataset.target.name], train_data.loc[:, dataset.target.name]
        learner.fit(X, y)

    with Timer() as predict:
        test_data = pd.read_parquet(dataset.test)
        X_test, y_test = test_data.loc[:, test_data.columns != dataset.target.name], test_data.loc[:, dataset.target.name]
        predictions = learner.predict(X_test)

    probabilities= None
    if config.type == 'classification':
        probabilities = learner.predict_proba(X_test)


    return result(
        output_file=config.output_predictions_file,
        predictions=predictions,
        probabilities=probabilities,
        truth=y_test,
        target_is_encoded=False,
        training_duration=training.duration,
        predict_duration=predict.duration,
    )

if __name__ == '__main__':
    call_run(run)