# Streamlit app entry point
import streamlit as st
from utils import StockAPI

# Load the StockAPI Client
client = StockAPI()

# Setup streamlit page
st.set_page_config(page_title="Stock Market Project", layout="wide")

# Add a heading
st.title("Stock Market Project")
st.subheader("by Utkarsh Gaikwad")

# Create a text input for company search
company_name = st.text_input("Company Name")

# Use search query to search company name
if company_name:
    search = client.search_symbol(company_name)
    all_symbols = search["1. symbol"].to_list()
    selected_symbol = st.selectbox("Symbol", options=all_symbols)
    company_info = search.query(f"`1. symbol` == '{selected_symbol}'")
    st.dataframe(company_info)

    # Create a submit button to plot the chart
    submit = st.button("Plot", type="primary")

    # If submit button pressed plot the chart
    if submit:
        daily_df = client.stock_prices(symbol=selected_symbol)
        st.dataframe(daily_df.head())
        fig = client.plot_chart(df=daily_df)
        st.plotly_chart(fig)
