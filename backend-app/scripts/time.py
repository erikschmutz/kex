import time;
from train import train_model, save_model
from config import make_config
import sys


config = make_config("""{
    "target":"example",
    "activation":"relu",
    "solver":"adam"
}""")



start_time = time.time()
model = train_model(config)
end_time = time.time()

print("Took " , (end_time-start_time), "s to train model...", file=sys.stderr)