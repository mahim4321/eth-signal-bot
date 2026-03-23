import streamlit as st
import streamlit.components.v1 as components
import requests

# ১. প্রো-ট্রেডার ইন্টারফেস
st.set_page_config(page_title="Master AI Pro Elite", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    .signal-engine, .exit-engine {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .exit-safe { background-color: #1e2329; border: 1px solid #00ff88; color: #00ff88; }
    .exit-danger { background-color: #ff4b4b; border: 2px solid white; color: white; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
    h2, h3 { color: #f0b90b !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ২. স্মার্ট ইঞ্জিন (News, BTC & Exit Logic)
def get_market_data():
    try:
        btc = requests.get("https://api.binance.com/api/3/ticker/24hr?symbol=BTCUSDT").json()
        eth = requests.get("https://api.binance.com/api/3/ticker/24hr?symbol=ETHUSDT").json()
        btc_change = float(btc['priceChangePercent'])
        eth_change = float(eth['priceChangePercent'])
        return btc_change, eth_change
    except:
        return 0.0, 0.0

btc_c, eth_c = get_market_data()

st.markdown("<h2>🤖 Master AI Pro: Elite Mode</h2>", unsafe_allow_html=True)

# ৩. মেইন সিগন্যাল ও ইমার্জেন্সি এক্সিট বাটন
col_top1, col_top2 = st.columns(2)

with col_top1:
    # মার্কেট এন্ট্রি ভার্ডিক্ট
    if btc_c > -1.5:
        st.markdown(f'<div class="signal-engine" style="background-color: #00ff88; color: black; font-size: 22px;">✅ মার্কেট কন্ডিশন: নিরাপদ</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="signal-engine" style="background-color: #f0b90b; color: black; font-size: 22px;">⚠️ মার্কেট অস্থির: সাবধানে থাকুন</div>', unsafe_allow_html=True)

with col_top2:
    # ইমার্জেন্সি এক্সিট ইঞ্জিন
    if eth_c < -4.0 or btc_c < -4.0:
        st.markdown(f'<div class="exit-engine exit-danger" style="font-size: 22px;">🚨 EMERGENCY EXIT: এখনই ট্রেড ক্লোজ করুন!</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="exit-engine exit-safe" style="font-size: 22px;">🛡️ Exit Status: হোল্ড করুন (Safe)</div>', unsafe_allow_html=True)

st.divider()

# ৪. ট্রেডিং উইজেটস
col1, col2 = st.columns([1.2, 1])

with col1:
    st.write("### 📡 Technical Analysis (15m)")
    components.html(f"""
        <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with col2:
    st.write("### 📊 Market Depth (ETH)")
    components.html("""
        <iframe src="https://s.tradingview.com/embed-widget/symbol-overview/?symbols=BINANCE%3AETHUSDT&colorTheme=dark&autosize=true" width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

st.divider()

# ৫. প্রফেশনাল চার্ট
st.write("### 📈 Live Execution Chart")
components.html("""
    <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="550" frameborder="0"></iframe>
""", height=560)
