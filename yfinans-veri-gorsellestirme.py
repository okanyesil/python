import yfinance as yf
import pandas as pd
import numpy as np
stock = yf.Ticker('AMZN')

data = stock.history(period='1d', start='2020-1-1', end='2020-12-20')
