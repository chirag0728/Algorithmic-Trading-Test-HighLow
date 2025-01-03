def track_high_low(data):
    """
    Tracks the highest and lowest prices of the day from stock data.

    Parameters:
    - data (pd.DataFrame): A DataFrame containing stock data with 'High' and 'Low' columns.

    Returns:
    - high (float): The highest price of the day.
    - low (float): The lowest price of the day.
    """
    try:
        high = data['High'].max()  # Find the highest price
        low = data['Low'].min()   # Find the lowest price
        return high, low
    except KeyError as e:
        print(f"KeyError: Missing column in data: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error while tracking high/low: {e}")
        return None, None
