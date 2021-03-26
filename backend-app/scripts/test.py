from sklearn.metrics import confusion_matrix
from dataset import load_dataset
from train import load_model

def test_model(model, x_test, y_test):
    preds = model.predict(x_test)
    score = model.score(x_test, y_test)

    labels = y_test.values

    for i in range(len(preds)):
        print(f"[{i}]\nLabel: {labels[i]}\nPredicted: {preds[i]}\n")

    print(f"Total score {score}\n")


