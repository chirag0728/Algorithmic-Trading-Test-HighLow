def analyze_directionality(ema_8, ema_9, ema_200):
    if ema_8 > ema_9 > ema_200:
        return "Uptrend"
    elif ema_8 < ema_9 < ema_200:
        return "Downtrend"
    else:
        return "Sideways"
