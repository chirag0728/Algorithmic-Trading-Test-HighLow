from sklearn.metrics import mean_absolute_error

def evaluate_mae(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    print(f"Mean Absolute Error: {mae}")
    return mae
