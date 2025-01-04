import pandas as pd
from src.data_fetching import fetch_data_yfinance
from src.data_preprocessing import preprocess_with_patterns
from src.model import train_or_load_model, predict_with_model
from joblib import load, dump
import os

def main(ticker="TSLA"):
    try:
        # Ensure the outputs directory exists
        os.makedirs("outputs", exist_ok=True)

        # Fetch data
        print(f"Fetching data for {ticker}...")
        data = fetch_data_yfinance(ticker)
        if data.empty:
            print("No data available. Exiting.")
            return

        # Preprocess data
        print("Preprocessing data...")
        data = preprocess_with_patterns(data)

        # Debugging: Check columns after preprocessing
        print("Columns in data after preprocessing:", data.columns)

        # Prepare features (X) and target (y)
        required_columns = [f"High_{ticker}", f"Low_{ticker}"]
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Required target columns {required_columns} are missing from the data.")

        X = data.drop(columns=required_columns + [f"Close_{ticker}"], errors='ignore')
        y = data.loc[:, required_columns]

        # Ensure X contains only numeric columns
        X = X.select_dtypes(include=['number'])

        # Use the last row for tomorrow's prediction
        X_tomorrow = X.iloc[-1:]

        # Train or load the model
        model_path = f"outputs/{ticker}_model.pkl"
        retrain_model = False
        if os.path.exists(model_path):
            print("Loading existing model...")
            try:
                # Try loading both model and feature names
                model, trained_features = load(model_path)

                # Align current features with trained features
                X = X.reindex(columns=trained_features, fill_value=0)

                # Check for feature mismatch
                if set(trained_features) != set(X.columns):
                    print("Feature mismatch detected. Retraining the model...")
                    retrain_model = True
            except ValueError:
                print("Legacy model detected. Retraining the model...")
                retrain_model = True
        else:
            print("Training a new model...")
            retrain_model = True

        if retrain_model:
            model = train_or_load_model(X.iloc[:-1], y.iloc[:-1], model_path)

        # Predict tomorrow's high and low
        predictions = predict_with_model(model, X_tomorrow)
        print(f"Predictions for {ticker} tomorrow:")
        print(f"High: {predictions[0][0]:.2f}, Low: {predictions[0][1]:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
