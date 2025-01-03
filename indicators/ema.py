import pandas as pd

def calculate_ema(prices, period):
    """
    Calculates the EMA for a given period and returns the last value.

    Parameters:
    - prices (pd.Series): A series of prices.
    - period (int): The EMA period.

    Returns:
    - float: The last value of the calculated EMA.
    """
    ema_series = prices.ewm(span=period, adjust=False).mean()
    return ema_series.iloc[-1]  # Return the last value
