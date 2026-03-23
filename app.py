import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="ETH Pro Signal", layout="wide")

def get_live_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": "ETHUSDT", "interval": "15m", "limit": 100}
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if not data or 'code' in data: # ডাটা খালি কি না চেক
            return None
        df = pd.DataFrame(data, columns=['time', 'open', 'high', 'low', 'close', 'vol', 'close_time', 'q_vol', 'trades', 't_base', 't_quote', 'ignore'])
        df['close'] = df['close'].astype(float)
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        return df
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None

st.title("📊 ETH Real-Time Pro Signal")

# বাটন ক্লিক করলে বা পেজ লোড হলে
df = get_live_data()

if df is not None and not df.empty:
    current_price = df['close'].iloc[-1]
    
    # RSI Calculation
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs)).iloc[-1]
    
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
    c1.metric("Current Price", f"${current_price:.2f}")
    c2.metric("RSI (14)", f"{rsi:.2f}")

    fig = go.Figure(data=[go.Candlestick(x=df['time'], open=df['open'].astype(float), high=df['high'].astype(float), low=df['low'].astype(float), close=df['close'])])
    fig.update_layout(template="plotly_dark", height=400, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("বিন্যান্স থেকে ডাটা লোড হচ্ছে না। দয়া করে ১ মিনিট পর 'Update' দিন।")

if st.button('Update Signal Now'):
    st.rerun()
