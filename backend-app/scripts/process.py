from sklearn.model_selection import train_test_split
from keras.applications.vgg16 import preprocess_input
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import pickle
import os

IMG_SIZE = 224

resnet50 = ResNet50(weights='imagenet', include_top=False)

def get_features(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    resnet_features = resnet50.predict(img_data)
    return resnet_features

def make_dataset(data_dir):
    features = {}

    for label in os.listdir(data_dir):
        features[label] = []

        img_dir = os.path.join(data_dir, label)
        for img in tqdm(os.listdir(img_dir)):

            # Training/Banana/img.jpg
            img_path = os.path.join(img_dir, img)

            feats = get_features(img_path)
            features[label].append(feats.flatten())

    dataset = pd.DataFrame()

    for label, feats in features.items():
        temp_df = pd.DataFrame(feats)
        temp_df['label'] = label
        dataset = dataset.append(temp_df, ignore_index=True)

    dataset.head()

    X = dataset.drop('label', axis=1)
    Y = dataset.label

    return [X, Y]

def process(config):
    data_dir = f'./{config.target}/data'
    dataset_save = f'./{config.target}/dataset.bin'

    [X, Y] = make_dataset(data_dir)
    split_dataset=train_test_split(X, Y, test_size=0.25,random_state=42)

    pickle.dump(split_dataset, open(dataset_save, 'wb'))

def load_dataset(config):
    dataset_save = f'./{config.target}/dataset.bin'
    return pickle.load(open(dataset_save, 'rb'))






