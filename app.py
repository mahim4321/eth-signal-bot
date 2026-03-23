import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="ETH Pro Signal", layout="wide")

def get_data_direct():
    # সরাসরি ব্রাউজার স্টাইল ডাটা রিকোয়েস্ট
    url = "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=15m&limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=['time', 'open', 'high', 'low', 'close', 'vol', 'close_time', 'q_vol', 'trades', 't_base', 't_quote', 'ignore'])
            df['close'] = df['close'].astype(float)
            df['time'] = pd.to_datetime(df['time'], unit='ms')
            return df
    except:
        return None
    return None

st.title("📊 ETH Real-Time Pro Signal")

df = get_data_direct()

if df is not None:
    current_price = df['close'].iloc[-1]
    
    # RSI
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rsi = 100 - (100 / (1 + (gain / loss))).iloc[-1]
    
    # EMA 20
    ema_20 = df['close'].ewm(span=20, adjust=False).mean().iloc[-1]
    
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
    fig.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("ডাটা পাওয়া যাচ্ছে না। দয়া করে আপনার ফোনের ইন্টারনেট (LTE) একবার অন-অফ করে নিচের বাটনে ক্লিক করুন।")

if st.button('Update Now'):
    st.rerun()
