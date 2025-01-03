from config.settings import STOCKS
from data.fetch_data import fetch_historical_data
from models.predict_high_low import predict_high_low
from utils.formatter import format_prediction_output

def main():
    print("📈 Stock Predictor - High/Low Prediction\n")
    for stock in STOCKS:
        print(f"Fetching data and predicting for {stock}...")
        
        # Predict high and low
        predicted_high, predicted_low = predict_high_low(stock)
        
        # Display results
        output = format_prediction_output(stock, predicted_high, predicted_low)
        print(output)

if __name__ == "__main__":
    main()
