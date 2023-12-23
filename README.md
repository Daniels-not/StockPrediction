# Stock Predictions App 🔀

![App Screenshot](https://github.com/Daniels-not/StockPrediction/blob/main/images/index%20%C2%B7%20Streamlit%20(1).png)

This Streamlit app enables users to make stock predictions using the Prophet library. It provides an interactive interface for selecting a stock dataset, adjusting the prediction duration, and visualizing both raw and forecasted data.

## Usage

1. **Select Dataset for Prediction:** Use the dropdown menu to choose a stock dataset from a predefined list.

2. **Set Prediction Duration:** Adjust the slider to specify the number of years for future predictions (between 1 and 10 years).

3. **Loading Data:** The app displays loading messages while the selected stock data is being loaded. Once completed, it confirms the loading process.

4. **Raw Data Visualization:** View the last rows of the loaded data and a plot of the raw data.

5. **Forecasting Dataset:** Prepare the dataset for forecasting using the Prophet library.

6. **Create and Fit Prophet Model:** Create a Prophet model and fit it with the training data.

7. **Predict Future Data:** Generate future dates and predict corresponding stock prices.

8. **Display Forecast Results:** View the last rows of the forecasted data and visualize forecast components.

## Installation

```bash
pip install -r requirements.txt
```

Install the required dependencies using the provided requirements.txt file.

## How to Run

```bash
streamlit run your_app_name.py
```

Make sure to replace `your_app_name.py` with the actual name of your Streamlit app file.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Prophet](https://facebook.github.io/prophet/)
- [Plotly](https://plotly.com/)

## Emoji Guide

- 🔀: Streamlit App
- 🏓: Raw Data
- 🏰: Forecast Data
- 🥤: Forecast Components
- 🔃: Loading Data
- 🧭: Loading Data Completed
