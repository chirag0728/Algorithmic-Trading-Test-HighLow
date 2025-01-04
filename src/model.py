from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load
import os

def train_or_load_model(X, y, model_path):
    """
    Trains or loads a RandomForest model.
    Args:
        X (pd.DataFrame): Features.
        y (pd.DataFrame): Targets.
        model_path (str): Path to save or load the model.
    Returns:
        model: Trained model.
    """
    if os.path.exists(model_path):
        print("Loading existing model...")
        return load(model_path)

    print("Training a new model...")
    model = RandomForestRegressor()
    model.fit(X, y)

    # Save the model and feature names
    dump((model, X.columns.tolist()), model_path)
    print(f"Model saved at {model_path}.")
    return model

def predict_with_model(model, X):
    """
    Makes predictions with the trained model.
    Args:
        model: Trained model.
        X (pd.DataFrame): Features.
    Returns:
        np.ndarray: Predictions.
    """
    print("Making predictions...")
    return model.predict(X)
