from sklearn.model_selection import train_test_split
from dataset import make_dataset, save_dataset, load_dataset
from train import train_model, save_model, load_model
from test import test_model
from config import make_config
import json


config = make_config("""{
    "target":"example",
    "activation":"relu",
    "solver":"adam"
}""")

print("- Processing dataset -")
X,Y = make_dataset(config)
dataset = train_test_split(X, Y, test_size=0.25,random_state=42)

print("- Saving dataset -")
save_dataset(config, dataset)

print("- Loading dataset -")
dataset = load_dataset(config)

print("- Training model -")
model = train_model(config, dataset)

print("- Saving model -")
save_model(config, model)

print("- Loading model -")
model = load_model(config)

print("- Testing model -")
test_model(model, dataset)
