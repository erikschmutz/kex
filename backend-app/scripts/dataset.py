from keras.applications.vgg16 import preprocess_input
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from tqdm import tqdm
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

def make_dataset(config, limit=None):
    features = {}
    count = 0

    for label in os.listdir(config.data_dir):
        features[label] = []

        img_dir = os.path.join(config.data_dir, label)
        for img in tqdm(os.listdir(img_dir)):

            # Training/Banana/img.jpg
            img_path = os.path.join(img_dir, img)

            feats = get_features(img_path)
            features[label].append(feats.flatten())

            count += 1

            if limit != None and count > limit:
                break
        else:
            continue

        break

    dataset = pd.DataFrame()

    for label, feats in features.items():
        temp_df = pd.DataFrame(feats)
        temp_df['label'] = label
        dataset = dataset.append(temp_df, ignore_index=True)

    dataset.head()

    X = dataset.drop('label', axis=1)
    Y = dataset.label

    return X,Y

def save_dataset(config, dataset):
    pickle.dump(dataset, open(config.dataset_save, 'wb'))

def load_dataset(config):
    return pickle.load(open(config.dataset_save, 'rb'))






