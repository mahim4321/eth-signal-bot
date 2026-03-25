import streamlit as st
import streamlit.components.v1 as components
import requests
import time
from streamlit_autorefresh import st_autorefresh

# ১. অটো-রিফ্রেশ সেটআপ
st.set_page_config(page_title="BTC Master AI Pro", layout="wide")
st_autorefresh(interval=30000, limit=100, key="btc_refresher")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    .status-card {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #f0b90b;
        background: #1e2329;
        margin-bottom: 20px;
    }
    .timer-text { font-size: 14px; color: #787b86; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# ২. বিটকয়েন লাইভ ডাটা
def get_btc_data():
    try:
        resp = requests.get("https://api.binance.com/api/3/ticker/24hr?symbol=BTCUSDT").json()
        return float(resp['lastPrice']), float(resp['priceChangePercent'])
    except:
        return 0.0, 0.0

btc_p, btc_c = get_btc_data()

# ৩. হেডার
st.markdown("<h2 style='text-align: center; color: #f0b90b;'>⚡ BTC Master AI: GitHub Edition</h2>", unsafe_allow_html=True)
st.markdown(f"<p class='timer-text'>🔄 Last Update: {time.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# ৪. সিগন্যাল কার্ড
if btc_c < -2.0:
    st.markdown(f'<div class="status-card" style="border-color: #ff4b4b; color: #ff4b4b;">🛑 বিপদ: BTC {btc_c}% ডাউন!</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="status-card" style="color: #00ff88;">✅ মার্কেট স্থিতিশীল (BTC: ${btc_p})</div>', unsafe_allow_html=True)

# ৫. ট্রেডিং ভিউ উইজেটস
col1, col2 = st.columns(2)
with col1:
    st.write("### ⏱️ BTC Fast (1m)")
    components.html('<iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3ABTCUSDT&interval=1m&colorTheme=dark&width=100%25&height=380" frameborder="0"></iframe>', height=400)
with col2:
    st.write("### 🛡️ BTC Confirm (15m)")
    components.html('<iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3ABTCUSDT&interval=15m&colorTheme=dark&width=100%25&height=380" frameborder="0"></iframe>', height=400)

st.divider()
st.write("### 📈 Live BTC Chart")
components.html('<iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE%3ABTCUSDT&interval=15&theme=dark" width="100%" height="500" frameborder="0"></iframe>', height=510)
