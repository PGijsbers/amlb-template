from amlb.benchmark import TaskConfig
from amlb.data import Dataset
from amlb.utils import call_script_in_same_dir
from frameworks.shared.caller import run_in_venv


def setup(*args, **kwargs):
    call_script_in_same_dir(__file__, "setup.sh", *args, **kwargs)

def run(dataset: Dataset, config: TaskConfig):
    data = dict(
        train=dataset.train.data_path('parquet'),
        test=dataset.test.data_path('parquet'),
        target=dict(
            name=dataset.target.name,
            classes=dataset.target.values
        ),
        problem_type=dataset.type.name,
    )
    return run_in_venv(
       __file__,
    "exec.py",

        input_data=data, dataset=dataset, config=config
    )