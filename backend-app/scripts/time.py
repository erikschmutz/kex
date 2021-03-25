import time
from train import train_model, save_model
from dataset import make_dataset, save_dataset, load_dataset
from config import make_config
import sys


config = make_config("""{
    "target":"example",
    "activation":"relu",
    "solver":"adam"
}""")


dataset = make_dataset(config)
print("done with dataset...")
start_time = time.time()
model = train_model(config, dataset)
end_time = time.time()

print("Took ", (end_time-start_time), "s to train model...")
