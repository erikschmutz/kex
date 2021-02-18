from sklearn.metrics import confusion_matrix
from dataset import load_dataset
from train import load_model

def test_model(config):
    _,x_test,_,y_test = load_dataset(config)
    model = load_model(config)

    print("- Testing model -")
    preds = model.predict(x_test)
    score = model.score(x_test, y_test)

    labels = y_test.values

    for i in range(len(preds)):
        print(f"[{i}]\nLabel: {labels[i]}\nPredicted: {preds[i]}\n")

    print(f"Total score {score}\n")


