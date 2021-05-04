import time
from train import train_model, save_model
from dataset import make_dataset, save_dataset, load_dataset
from config import make_config
import sys

config = make_config("""{
    "target":"example",
    "activation":"relu",
    "solver":"adam",
    "limit": 1000
}""")

try:
    dataset = load_dataset(config)
except:
    dataset = make_dataset(config)
    save_dataset(config, dataset)

print("loaded dataset")

def features():
    start_time = time.time()
    make_dataset(config)
    end_time = time.time()
    return end_time-start_time

def train(dataset):
    X,Y = dataset
    start_time = time.time()
    train_model(config, X, Y)
    end_time = time.time()
    return end_time-start_time

def train_loop():
    incr = 25
    datastr = ""
    for i in range(incr, config.limit+incr, incr):
        print(f"incr {i}")
        time = train_specfic(i)
        timestr = f'{i} {time}\n'
        print(timestr)
        datastr += timestr

    with open(f'train_{config.name}.dat', 'w') as file:
        file.write(datastr)

def train_specfic(i):
    X,Y = dataset
    Xn = X[0:i]
    Yn = Y[0:i]

    return train([Xn, Yn])

def train_all():
    X,Y = dataset
    start_time = time.time()
    train_model(config, X, Y)
    end_time = time.time()
    print("Took ", (end_time-start_time), "s to train model...")

arg = sys.argv[1]
if arg == "train_loop": train_loop()
elif arg == "train_all":  train_all()
elif arg == "features": features()

exit()
