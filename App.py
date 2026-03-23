import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="ETH Signal Bot", layout="wide")

def get_live_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": "ETHUSDT", "interval": "15m", "limit": 100}
    try:
        response = requests.get(url, params=params)
        df = pd.DataFrame(response.json(), columns=['time', 'open', 'high', 'low', 'close', 'vol', 'close_time', 'q_vol', 'trades', 't_base', 't_quote', 'ignore'])
        df['close'] = df['close'].astype(float)
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        return df
    except: return None

st.title("📊 ETH Real-Time Pro Signal")

if st.button('Update Signal Now'):
    df = get_live_data()
    if df is not None:
        current_price = df['close'].iloc[-1]
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rsi = 100 - (100 / (1 + (gain / loss))).iloc[-1]
        ema_20 = df['close'].ewm(span=20, adjust=False).mean().iloc[-1]
        
        # সিগন্যাল লজিক
        if rsi < 38 and current_price > ema_20:
            signal, color = "🚀 BUY", "green"
        elif rsi > 62 or current_price < ema_20:
            signal, color = "🔴 SELL", "red"
        else:
            signal, color = "🟡 WAIT", "gray"

        st.markdown(f"<h1 style='text-align: center; color: {color}; font-size: 80px;'>{signal}</h1>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.metric("Price", f"${current_price:.2f}")
        c2.metric("RSI", f"{rsi:.2f}")

        fig = go.Figure(data=[go.Candlestick(x=df['time'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
        fig.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig, use_container_width=True)
