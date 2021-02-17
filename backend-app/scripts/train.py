# https://www.kaggle.com/shivamb/cnn-architectures-vgg-resnet-inception-tl

import pickle
from process import load_dataset
from sklearn.neural_network import MLPClassifier

def train(config):
    model_save = f"./{config.target}/{config.activation}.bin"

    try:
        x_train,_,y_train,_ = load_dataset(config.target)

        model = MLPClassifier(hidden_layer_sizes=(100, 10), activation=config.activation, solver=config.solver)
        model.fit(x_train, y_train)

        pickle.dump(model, open(model_save, 'wb'))
    except:
        return False

def load_model(config):
    model_save = f"./{config.target}/{config.activation}.bin"
    return pickle.load(open(model_save, 'rb'))

