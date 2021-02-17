
from process import load_dataset
from train import load_model

def test(config):
    _,x_test,_,y_test = load_dataset(config)
    model = load_model(config)

    preds = model.predict(x_test)
    result = model.score(x_test, y_test)

    print(f"Total score {result}\n")

    for i in range(len(preds)):
        print(f"[{i}] Predicted: {preds[i]}, Label: {y_test[i]}\n")


