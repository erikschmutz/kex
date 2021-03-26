import time
from sklearn.model_selection import train_test_split
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

def time_features(limit):
    start_time = time.time()
    make_dataset(config, limit)
    end_time = time.time()
    return end_time-start_time

def time_features_loop():
    for i in range(0, 10):
        limit = 10*i
        time = time_features(limit)
        print(time)

def time_train(dataset):
    X,Y = dataset
    start_time = time.time()
    train_model(config, X, Y)
    end_time = time.time()
    return end_time-start_time

def time_train_loop():
    limit = 200
    incr = 10
    datastr = ""
    X,Y = dataset
    for i in range(incr, limit+incr, incr):
        Xn = X[0:i]
        Yn = Y[0:i]

        time = time_train([Xn, Yn])
        timestr = f'{i} {time}\n'
        print(timestr)
        datastr += timestr

    with open(f'train_{config.name}_{limit}.dat', 'w') as file:
        file.write(datastr)

def time_train_all():
    time = time_train(dataset)
    print("Took " , time, "s to train model...", file=sys.stderr)

arg = sys.argv[1]
if arg == "features": time_features_loop()
elif arg == "train_loop": time_train_loop()
elif arg == "train_all":  time_train_all()

