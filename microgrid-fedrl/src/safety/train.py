import csv
import json
import math
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), os.pardir, '..', 'data', 'safetynet', 'train.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'safety_model.pt')


def load_data(path):
    X, y = [], []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append([float(row['state']), float(row['action'])])
            y.append(int(row['label']))
    return X, y


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def train_log_reg(X, y, lr=0.5, epochs=2000):
    w = [0.0, 0.0]
    b = 0.0
    n = len(X)
    for _ in range(epochs):
        dw = [0.0, 0.0]
        db = 0.0
        for xi, yi in zip(X, y):
            z = w[0] * xi[0] + w[1] * xi[1] + b
            p = sigmoid(z)
            error = p - yi
            dw[0] += error * xi[0]
            dw[1] += error * xi[1]
            db += error
        w[0] -= lr * dw[0] / n
        w[1] -= lr * dw[1] / n
        b -= lr * db / n
    return {'w': w, 'b': b}


def predict(model, X):
    preds = []
    for xi in X:
        z = model['w'][0] * xi[0] + model['w'][1] * xi[1] + model['b']
        p = sigmoid(z)
        preds.append(1 if p >= 0.5 else 0)
    return preds


def f1_score(y_true, y_pred):
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp == 1)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
    if tp + fp == 0 or tp + fn == 0:
        return 0.0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def main():
    X, y = load_data(DATA_PATH)
    model = train_log_reg(X, y)
    preds = predict(model, X)
    f1 = f1_score(y, preds)
    print(f"Training F1: {f1:.2f}")
    with open(MODEL_PATH, 'w') as f:
        json.dump(model, f)
    if f1 < 0.9:
        print('Warning: F1 below 0.90')


if __name__ == '__main__':
    main()
