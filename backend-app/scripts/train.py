# https://www.kaggle.com/shivamb/cnn-architectures-vgg-resnet-inception-tl

import pickle
from dataset import load_dataset
from sklearn.neural_network import MLPClassifier

def train_model(config):
    x_train, _, y_train, _ = load_dataset(config)

    # print("- Training model -")
    model = MLPClassifier(hidden_layer_sizes=(100, 10), activation=config.activation, solver=config.solver)
    model.fit(x_train, y_train)

    return model

def save_model(config, model):
    # print("- Saving model -")
    pickle.dump(model, open(config.model_save, 'wb'))

def load_model(config):
    # print("- Loading model -")
    return pickle.load(open(config.model_save, 'rb'))

