import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go

st.set_page_config(page_title="Real-Time Stock Dashboard", layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

@st.cache_data
def load_data():
    # UPDATE YOUR PASSWORD HERE:
    db_password = "0550" 
    engine = create_engine(f"mysql+pymysql://root:{db_password}@localhost/stock_portfolio")
    df = pd.read_sql("SELECT * FROM live_stocks", engine)
    return df

df = load_data()

st.sidebar.header("User Input Options")
selected_stock = st.sidebar.selectbox("Select a Stock", df['Ticker'].unique())

filtered_df = df[df['Ticker'] == selected_stock]

st.subheader(f"Data for {selected_stock}")

if not filtered_df.empty:
    latest_close = filtered_df['Close'].iloc[-1]
    latest_open = filtered_df['Open'].iloc[-1]
    st.metric(label="Latest Closing Price", value=f"₹{latest_close:.2f}", delta=f"₹{latest_close - latest_open:.2f}")

    fig = go.Figure(data=[go.Candlestick(
        x=filtered_df['Date'],
        open=filtered_df['Open'],
        high=filtered_df['High'],
        low=filtered_df['Low'],
        close=filtered_df['Close'],
        name="Market Data"
    )])

    fig.update_layout(title=f"{selected_stock} Price Trend (Last 1 Year)", xaxis_title="Date", yaxis_title="Price (INR)")
    st.plotly_chart(fig, use_container_width=True)
    
    if st.checkbox("Show Raw Data from MySQL"):
        st.write(filtered_df.tail())
else:
    st.warning("No data found.")