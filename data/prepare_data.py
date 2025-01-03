def prepare_features(data):
    data['Time'] = data.index.hour * 60 + data.index.minute  # Time in minutes
    data['Range'] = data['High'] - data['Low']
    data['SMA'] = data['Close'].rolling(window=10).mean()
    data['EMA'] = data['Close'].ewm(span=10).mean()
    data.dropna(inplace=True)
    return data[['Open', 'Close', 'Volume', 'Time', 'SMA', 'EMA']], data['High'], data['Low']
