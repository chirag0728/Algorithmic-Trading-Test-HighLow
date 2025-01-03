import joblib
from data.fetch_data import fetch_historical_data
from data.prepare_data import prepare_features

def predict_high_low(stock):
    """
    Predicts the high and low for the next trading day.

    Args:
        stock (str): Ticker symbol of the stock.

    Returns:
        Tuple[float, float]: Predicted high and low prices for the next trading day.
    """
    # Load trained models
    high_model = joblib.load(f'models/{stock}_high_model.pkl')
    low_model = joblib.load(f'models/{stock}_low_model.pkl')

    # Fetch the most recent daily data
    data = fetch_historical_data(stock, interval="1d", period="1mo")
    if data is None or data.empty:
        raise ValueError(f"No data available for {stock}.")

    # Prepare features
    X, _, _ = prepare_features(data)
    latest_features = X.iloc[-1].values.reshape(1, -1)

    # Predict
    predicted_high = high_model.predict(latest_features)[0]
    predicted_low = low_model.predict(latest_features)[0]

    return predicted_high, predicted_low
