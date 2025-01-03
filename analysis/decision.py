def analyze_directionality(ema_8, ema_9, ema_200):
    """
    Analyzes the stock's directionality based on EMA relationships.

    Parameters:
    - ema_8 (float): Exponential Moving Average (8-period).
    - ema_9 (float): Exponential Moving Average (9-period).
    - ema_200 (float): Exponential Moving Average (200-period).

    Returns:
    - str: A string indicating the direction ("Uptrend", "Downtrend", or "Sideways").
    """
    try:
        if ema_8 > ema_9 > ema_200:
            return "Uptrend"
        elif ema_8 < ema_9 < ema_200:
            return "Downtrend"
        else:
            return "Sideways"
    except Exception as e:
        print(f"Error analyzing directionality: {e}")
        return "Error"
