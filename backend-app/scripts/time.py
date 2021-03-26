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

try:
    dataset = load_dataset(config)
except:
    dataset = make_dataset(config)
    save_dataset(config, dataset)

def features(limit):
    start_time = time.time()
    make_dataset(config, limit)
    end_time = time.time()
    return end_time-start_time

def features_loop():
    for i in range(0, 10):
        limit = 10*i
        time = features(limit)
        print(time)

def train(dataset):
    X,Y = dataset
    start_time = time.time()
    train_model(config, X, Y)
    end_time = time.time()
    return end_time-start_time

def train_loop():
    limit = 200
    incr = 10
    datastr = ""
    for i in range(incr, limit+incr, incr):
        time = train_specfic(i)
        timestr = f'{i} {time}\n'
        print(timestr)
        datastr += timestr

    with open(f'train_{config.name}_{limit}.dat', 'w') as file:
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
if arg == "features_loop": features_loop()
elif arg == "train_loop": train_loop()
elif arg == "train_all":  train_all()

exit()
