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

## showcasing line charts

st.write(
    """
    ## Daily Closing Prices on a Line Chart:
    """
)

st.line_chart(ticker_df.Close)

st.write(
    """
    ## Daily Volume Prices on a Line Chart:
    """
)

st.line_chart(ticker_df.Volume)

## Layout

col1, col2 = st.columns(2)

with col1:
    st.header('Daily Closing Prices on a Line Chart')
    st.line_chart(ticker_df.Close)
with col2:
    st.header('Daily Volume Prices on a Line Chart')
    st.line_chart(ticker_df.Volume)
    