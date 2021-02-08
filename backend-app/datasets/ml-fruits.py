# https://www.kaggle.com/shivamb/cnn-architectures-vgg-resnet-inception-tl

from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

def _load_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

resnet50 = ResNet50(weights='imagenet', include_top=False)

def _get_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    resnet_features = resnet50.predict(img_data)
    return resnet_features

basepath = "fruits-360/Training/"
class1 = os.listdir(basepath + "Banana/")
class2 = os.listdir(basepath + "Strawberry/")

data = {'banana': class1[:10],
        'strawberry': class2[:10],
        'test': [class1[11], class2[11]]}

features = {"banana" : [], "strawberry" : [], "test" : []}
testimgs = []
for label, val in data.items():
    for k, each in enumerate(val):
        if label == "test" and k == 0:
            img_path = basepath + "/Banana/" + each
            testimgs.append(img_path)
        elif label == "test" and k == 1:
            img_path = basepath + "/Strawberry/" + each
            testimgs.append(img_path)
        else:
            img_path = basepath + label.title() + "/" + each
        feats = _get_features(img_path)
        features[label].append(feats.flatten())

dataset = pd.DataFrame()
for label, feats in features.items():
    temp_df = pd.DataFrame(feats)
    temp_df['label'] = label
    dataset = dataset.append(temp_df, ignore_index=True)
dataset.head()

y = dataset[dataset.label != 'test'].label
X = dataset[dataset.label != 'test'].drop('label', axis=1)

# Classifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline

model = MLPClassifier(hidden_layer_sizes=(100, 10))
pipeline = Pipeline([('low_variance_filter', VarianceThreshold()), ('model', model)])
pipeline.fit(X, y)

print ("Model Trained on pre-trained features")

preds = pipeline.predict(features['test'])

f, ax = plt.subplots(1, 2)
for i in range(2):
    ax[i].imshow(Image.open(testimgs[i]).resize((200, 200), Image.ANTIALIAS))
    ax[i].text(10, 180, 'Predicted: %s' % preds[i], color='k', backgroundcolor='red', alpha=0.8)
plt.show()












