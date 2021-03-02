from dataset import make_dataset, save_dataset
from train import train_model, save_model
from test import test_model
from config import make_config
import json

config = make_config("""{
    "target":"example",
    "activation":"relu",
    "solver":"adam"
}""")

dataset = make_dataset(config)
save_dataset(config, dataset)
model = train_model(config)
save_model(config, model)
test_model(config)