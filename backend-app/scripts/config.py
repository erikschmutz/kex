import json
from types import SimpleNamespace

def make_config(json_string):
    config = json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))
    config.name = f'{config.activation}_{config.solver}'
    config.model_save = f"./{config.target}/model_{config.name}.bin"
    config.data_dir = f'./{config.target}/data'
    config.dataset_save = f'./{config.target}/dataset_{config.name}.bin'
    return config
