import json
from types import SimpleNamespace

def make_config(json_string):
    config = json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))
    config.model_save = f"./{config.target}/models/{config.activation}.bin"
    config.data_dir = f'./{config.target}/data'
    config.dataset_save = f'./{config.target}/dataset.bin'
    return config
