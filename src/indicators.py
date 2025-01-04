import numpy as np

def candlestick_patterns(data):
    """
    Identifies candlestick patterns in OHLC data.
    Args:
        data (pd.DataFrame): OHLC data.
    Returns:
        pd.DataFrame: Data with an added 'Pattern' column.
    """
    print("Identifying candlestick patterns...")
    conditions = [
        (np.abs(data['Open'] - data['Close']) <= (data['High'] - data['Low']) * 0.1),  # Doji
        ((data['Close'] > data['Open']) & ((data['Low'] < data['Open']) & (data['Open'] - data['Low']) > 2 * (data['Close'] - data['Open']))),  # Hammer
        ((data['Close'] > data['Open'].shift(1)) & (data['Open'] < data['Close'].shift(1))),  # Engulfing
    ]
    patterns = ['Doji', 'Hammer', 'Engulfing']
    data['Pattern'] = np.select(conditions, patterns, default='None')
    print("Candlestick patterns identified.")
    return data
