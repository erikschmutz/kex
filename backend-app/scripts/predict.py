# Test prediction of new images

from process import get_features
from train import load_model

def predict(config, img_data):
    # write tmp img
    img_path = ""
    features = get_features(img_path)

    model = load_model(config)
    label = model.predict(features)

    return label

