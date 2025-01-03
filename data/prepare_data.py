import pandas as pd

def prepare_features(data):
    """
    Prepares features for machine learning models.

    Args:
        data (pd.DataFrame): Raw stock data.

    Returns:
        Tuple[pd.DataFrame, pd.Series, pd.Series]: Features (X), target high (y_high), target low (y_low).
    """
    data['Time'] = data.index.hour * 60 + data.index.minute  # Convert time to minutes
    data['Range'] = data['High'] - data['Low']
    data['SMA'] = data['Close'].rolling(window=10).mean()
    data['EMA'] = data['Close'].ewm(span=10).mean()
    data.dropna(inplace=True)

    X = data[['Open', 'Close', 'Volume', 'Time', 'SMA', 'EMA']]
    y_high = data['High']
    y_low = data['Low']

    return X, y_high, y_low
