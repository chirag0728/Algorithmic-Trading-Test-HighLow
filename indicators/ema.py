import pandas as pd

def calculate_ema(prices, period):
    return prices.ewm(span=period, adjust=False).mean().iloc[-1]
