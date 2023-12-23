import yfinance as yf
from config import variables
import streamlit as st


from plotly import graph_objs as go

@st.cache_data
def load_data(ticket):
    
    data = yf.download(ticket, variables.config_var["START_DATE"], variables.config_var["TODAY_DATE"])
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data):
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name='stock_open'))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name='stock_close'))
    fig.layout.update(title_text="Time Series Data ⌛", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)