def track_high_low(data):
    high = data['High'].max()
    low = data['Low'].min()
    return high, low
