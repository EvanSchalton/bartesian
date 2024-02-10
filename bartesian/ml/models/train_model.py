from tensorflow.keras.models import Model
from sklearn.model_selection import KFold
import numpy as np
import random

from bartesian.ml.interfaces.training_data import TrainingData


def train_model(
    model: Model,
    training_data: list[TrainingData],
    epochs: int,
):

    random.shuffle(training_data)
    X = np.array([i["input"] for i in training_data])
    Y = np.array([i["output"] for i in training_data])

    # K-Fold Cross-Validation
    kf = KFold(n_splits=len(X), shuffle=True)  # Leave-One-Out Cross-Validation
    fold_no = 1
    for train_index, val_index in kf.split(X):
        # Split data into training and validation sets
        X_train, X_val = X[train_index], X[val_index]
        Y_train, Y_val = Y[train_index], Y[val_index]

        # Train the model
        print(f"Training for fold {fold_no} ...")
        model.fit(X_train, Y_train, epochs=epochs)

        # Evaluate the model
        scores = model.evaluate(X_val, Y_val, verbose=0)
        print(f"Score for fold {fold_no}: {model.metrics_names[0]} of {scores}")
        fold_no += 1
