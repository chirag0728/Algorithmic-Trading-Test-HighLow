# **Stock Price Prediction Using Candlestick Patterns**

This project predicts the **High** and **Low** stock prices for the next trading day using historical OHLC data, candlestick patterns, and directionality indicators. The model dynamically fetches data, preprocesses it, and outputs precise predictions.

---

## **Features**
- **Dynamic Data Fetching**: Retrieves historical stock data automatically.
- **Candlestick Pattern Recognition**: Identifies patterns like Doji, Hammer, and Engulfing.
- **Directionality Indicator**: Determines market trends using rolling averages.
- **Feature Alignment**: Ensures model compatibility with evolving feature sets.
- **Model Retraining**: Automatically retrains the model when feature mismatch is detected.
- **Seamless Predictions**: Outputs the predicted High and Low prices for the next trading day.

---

## **Technologies Used**
- **Python**: Core programming language.
- **scikit-learn**: For model training and predictions.
- **yfinance**: To fetch historical OHLC data.
- **joblib**: To save and load the model efficiently.

---

## **Setup Instructions**

### Prerequisites
- Python 3.7+
- Virtual environment tools (e.g., `venv` or `conda`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:
   ```bash
   python main.py
   ```

---

## **Usage**

### Running the Program
The application predicts tomorrow's **High** and **Low** prices for a given stock ticker (default: SPY).

1. Fetch data, preprocess it, and make predictions:
   ```bash
   python main.py
   ```

2. Update the ticker symbol in `main.py` to predict for other stocks:
   ```python
   main(ticker="AAPL")
   ```

---

## **Project Structure**
```plaintext
project_root/
├── main.py               # CLI tool for running the prediction pipeline
├── data/                 # Directory for storing raw and processed data
├── outputs/              # Directory for saving the trained model
├── src/                  # Source code folder
│   ├── __init__.py
│   ├── data_fetching.py  # Fetches historical OHLC data
│   ├── data_preprocessing.py  # Preprocessing pipeline
│   ├── indicators.py     # Candlestick patterns and indicators
│   ├── model.py          # Model training and prediction logic
│   └── evaluation.py     # Evaluation utilities
├── requirements.txt      # List of project dependencies
├── .gitignore            # Specifies files to ignore in Git
└── README.md             # Project documentation
```

---

## **How It Works**
1. **Fetch Data**:
   - Downloads the last 365 days of OHLC data using `yfinance`.

2. **Preprocessing**:
   - Cleans the data, flattens multi-index columns, and adds:
     - **Candlestick patterns**.
     - **Directionality indicators**.

3. **Model Training**:
   - Trains a `RandomForestRegressor` to predict the High and Low prices for the next trading day.

4. **Predictions**:
   - Outputs tomorrow’s predicted **High** and **Low** prices.

---

## **Future Enhancements**
- Add additional technical indicators (e.g., RSI, MACD, Bollinger Bands).
- Incorporate sentiment analysis from news data.
- Support multi-day predictions.
- Enhance the model using gradient boosting or neural networks.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- [yfinance](https://github.com/ranaroussi/yfinance)
- [scikit-learn](https://scikit-learn.org)

---

### **Example Output**
```plaintext
Fetching data for SPY...
Fetching 365 days of data for SPY...
[*********************100%***********************]  1 of 1 completed
Preprocessing data...
Training a new model...
Predictions for SPY tomorrow:
High: 589.73, Low: 583.33
```

---
