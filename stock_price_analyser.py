import pandas as pd
import streamlit as st
import datetime
import yfinance as yf

st.write(

    """
    # Stock Price Analyser

    Shown are the stock prices of Apple Company
    """
)

ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d',
                                start='2019-01-01',
                                end='2023-02-14')

st.write(f"""
    ### {ticker_symbol}' stock price info:
""")

st.dataframe(ticker_df)