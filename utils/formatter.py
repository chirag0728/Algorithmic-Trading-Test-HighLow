def format_output(stock, high, low, direction, ema_8, ema_9, ema_200):
    output = f"""
    ┌─────────────────────────────────────────┐
    │               {stock} Summary              │
    ├─────────────────────────────────────────┤
    │ High of the Day       : {high:.2f}           │
    │ Low of the Day        : {low:.2f}           │
    │ Directionality        : {direction}          │
    ├─────────────────────────────────────────┤
    │ EMA (8)               : {ema_8:.2f}          │
    │ EMA (9)               : {ema_9:.2f}          │
    │ EMA (200)             : {ema_200:.2f}        │
    └─────────────────────────────────────────┘
    """
    return output
