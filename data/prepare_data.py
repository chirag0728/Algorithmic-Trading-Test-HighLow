def prepare_features(data):
    """
    Prepares features for next-day stock prediction.

    Args:
        data (pd.DataFrame): Raw daily stock data.

    Returns:
        Tuple[pd.DataFrame, pd.Series, pd.Series]: Features (X), target high (y_high), target low (y_low).
    """
    data['Previous_Close'] = data['Close'].shift(1)
    data['Previous_High'] = data['High'].shift(1)
    data['Previous_Low'] = data['Low'].shift(1)
    data['Previous_Open'] = data['Open'].shift(1)
    data['Previous_Volume'] = data['Volume'].shift(1)
    data['Range'] = data['High'] - data['Low']
    data['Volatility'] = (data['High'] - data['Low']) / data['Close']
    data.dropna(inplace=True)

    # Features (X) and targets (y_high, y_low)
    X = data[['Previous_Close', 'Previous_High', 'Previous_Low', 'Previous_Open', 'Previous_Volume', 'Volatility']]
    y_high = data['High']
    y_low = data['Low']

    return X, y_high, y_low
