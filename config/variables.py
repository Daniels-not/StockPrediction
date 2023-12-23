from datetime import date

config_var = {
    "START_DATE": "2015-01-01",
    "TODAY_DATE":  date.today().strftime("%Y-%m-%d"),
    "STOCKS": ("AAPL", "GOOG", "MSFT", "GME", "AMZN", "TSLA", "FB", "NFLX", "IBM", "NVDA", "PYPL", "INTC"),
    "DAYS_ON_YEAR": 365 
}