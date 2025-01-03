import joblib
from data.fetch_data import fetch_historical_data
from data.prepare_data import prepare_features

def predict_high_low(stock):
    # Load trained models
    high_model = joblib.load(f'models/{stock}_high_model.pkl')
    low_model = joblib.load(f'models/{stock}_low_model.pkl')

    # Fetch intraday data
    data = fetch_historical_data(stock, interval="5m", period="1d")
    X, _, _ = prepare_features(data)

    # Predict
    predicted_high = high_model.predict(X.tail(1))[0]
    predicted_low = low_model.predict(X.tail(1))[0]

    return predicted_high, predicted_low
