import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly

from plotly import graph_objs as go
from config import variables
from functions import data

# Set the title of the Streamlit app
st.title("Stock Predictions App 🔀")

# Allow the user to select a stock from the predefined list
select_stock = st.selectbox("Select Dataset for Prediction", variables.config_var["STOCKS"])

# Allow the user to set the number of years for prediction using a slider
num_years = st.slider("Years of Prediction: ", 1, 10)

# Calculate the total number of days for the given number of years
period = num_years * variables.config_var["DAYS_ON_YEAR"]

# Display a loading message while data is being loaded
data_load_state = st.text("Loading Data ... 🔃")

# Load the selected stock data
data_req = data.load_data(select_stock)

# Display a completion message after loading data
data_load_state = st.text("Loading Data Completed 🧭 ...")

# Display the last rows of the loaded data and plot the raw data
st.subheader("Raw Data 🏓")
st.write(data_req.tail())
data.plot_raw_data(data_req)

# Forecasting Dataset

# Extract relevant columns for forecasting (assumes 'Date' and 'Close' columns)
df_train = data_req[["Date", "Close"]]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Create a Prophet model and fit it with training data
m = Prophet()
m.fit(df_train)

# Create a future dataframe for prediction
future_data = m.make_future_dataframe(periods=period)

# Predict the future data
data_forecast = m.predict(future_data)

# Display the last rows of the forecasted data
st.subheader("Forecast Data 🏰")
st.write(data_forecast.tail())

# Display forecast components using a plotly chart
st.subheader("Forecast Components 🥤")
forecast_figure_one = plot_plotly(m, data_forecast)
st.plotly_chart(forecast_figure_one)

# Display forecast components using a built-in Prophet plot
st.subheader("Forecast Components 🥤")
forecast_figure_two = m.plot_components(data_forecast)
st.write(forecast_figure_two)

"""
Explanation:

1. **Select Stock:** Allows the user to choose a stock dataset for prediction from a predefined list.

2. **Set Prediction Duration:** A slider to set the number of years for future predictions.

3. **Load and Display Raw Data:** Loads the selected stock data, displays the last rows, and plots the raw data.

4. **Forecasting Dataset:** Prepares the dataset for forecasting using the Prophet library.

5. **Create and Fit Prophet Model:** Creates a Prophet model and fits it with the training data.

6. **Predict Future Data:** Generates future dates and predicts the corresponding stock prices.

7. **Display Forecast Results:** Shows the last rows of the forecasted data and visualizes forecast components.

This Streamlit app integrates user interaction, data loading, forecasting, and visualization for stock predictions.
"""