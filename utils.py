# Utility functions and classes
import requests
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

class StockAPI:

    def __init__(self):
        self.api_key = st.secrets["API_KEY"]
        self.url = "https://alpha-vantage.p.rapidapi.com/query"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
        }

    def search_symbol(self, company_name: str):
        querystring = {"datatype":"json","keywords":company_name,"function":"SYMBOL_SEARCH"}
        response = requests.get(self.url, headers=self.headers, params=querystring)
        data = response.json()
        df = pd.DataFrame(data["bestMatches"])
        search_data = df.iloc[:, 0:4]
        return search_data
    
    def stock_prices(self, symbol: str):
        querystring = {
            "function":"TIME_SERIES_DAILY","symbol":symbol,"outputsize":"compact","datatype":"json"
        }
        response = requests.get(self.url, headers=self.headers, params=querystring)
        data = response.json()
        daily = data["Time Series (Daily)"]
        daily_df = pd.DataFrame(daily).T
        daily_df = daily_df.astype(float)
        daily_df.index = pd.to_datetime(daily_df.index)
        daily_df.index.name = "Date"
        return daily_df

    def plot_chart(self, df: pd.DataFrame):
        fig = go.Figure(data=[
            go.Candlestick(
                x = df.index,
                open = df["1. open"],
                high = df["2. high"],
                low = df["3. low"],
                close = df["4. close"]
            )    
        ])

        fig.update_layout(width = 1000, height=800)
        return fig