def track_high_low(data):
    """
    Tracks the highest and lowest prices of the day from stock data.

    Parameters:
    - data (pd.DataFrame): A DataFrame containing stock data with 'High' and 'Low' columns.

    Returns:
    - high (float): The highest price of the day.
    - low (float): The lowest price of the day.
    """
    high = float(data['High'].max())  # Convert to float
    low = float(data['Low'].min())   # Convert to float
    return high, low
