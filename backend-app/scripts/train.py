# https://www.kaggle.com/shivamb/cnn-architectures-vgg-resnet-inception-tl
import pickle
from dataset import load_dataset
from sklearn.neural_network import MLPClassifier

def train_model(config, x_train, y_train):
    model = MLPClassifier(hidden_layer_sizes=(100, 10), activation=config.activation, solver=config.solver, max_iter=50, tol=1e-2)
    model.fit(x_train, y_train)

    return model

def save_model(config, model):
    pickle.dump(model, open(config.model_save, 'wb'))

def load_model(config):
    return pickle.load(open(config.model_save, 'rb'))

