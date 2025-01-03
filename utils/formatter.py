def format_prediction_output(stock, predicted_high, predicted_low):
    output = f"""
    ┌──────────────────────────────────────────┐
    │              {stock} Predictions              │
    ├──────────────────────────────────────────┤
    │ Predicted High       : {predicted_high:.2f}         │
    │ Predicted Low        : {predicted_low:.2f}         │
    └──────────────────────────────────────────┘
    """
    return output
