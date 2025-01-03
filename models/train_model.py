import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from data.fetch_data import fetch_historical_data
from data.prepare_data import prepare_features

def train_predictive_model(stock):
    # Load historical data
    data = fetch_historical_data(stock)
    X, y_high, y_low = prepare_features(data)
    
    # Split data
    X_train, X_test, y_train_high, y_test_high = train_test_split(X, y_high, test_size=0.2, random_state=42)
    _, _, y_train_low, y_test_low = train_test_split(X, y_low, test_size=0.2, random_state=42)

    # Train models
    high_model = RandomForestRegressor(n_estimators=100, random_state=42)
    low_model = RandomForestRegressor(n_estimators=100, random_state=42)
    high_model.fit(X_train, y_train_high)
    low_model.fit(X_train, y_train_low)

    # Evaluate
    high_mae = mean_absolute_error(y_test_high, high_model.predict(X_test))
    low_mae = mean_absolute_error(y_test_low, low_model.predict(X_test))
    print(f"High Prediction MAE: {high_mae}")
    print(f"Low Prediction MAE: {low_mae}")

    # Save models
    joblib.dump(high_model, f'models/{stock}_high_model.pkl')
    joblib.dump(low_model, f'models/{stock}_low_model.pkl')
