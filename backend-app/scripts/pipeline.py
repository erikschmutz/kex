
from process import process
from train import train
from test import test
import json

class Config:
    def __init__(self, json_data):
        config_json = json.load(json_data)

config = Config("{}")

process(config)
train(config)
test(config)
