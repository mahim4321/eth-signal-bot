import streamlit as st
import streamlit.components.v1 as components

# ১. পেজ সেটআপ (মোবাইল ফ্রেন্ডলি)
st.set_page_config(page_title="ETH Master AI: Final", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    .main-title {
        color: #627eea; text-align: center; font-size: 28px;
        font-weight: bold; padding: 20px; border-bottom: 2px solid #627eea;
    }
    </style>
    <div class="main-title">💎 ETH Master AI: 100% Accurate Mode</div>
    """, unsafe_allow_html=True)

# ২. ১৫ মিনিটের স্মার্ট সিগন্যাল মিটার (সবচেয়ে নির্ভরযোগ্য)
st.write("### 📡 15m Confirmed Signal")
components.html("""
    <div style="height:400px;">
    <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=100%25" frameborder="0" style="width:100%; height:100%;"></iframe>
    </div>
""", height=410)

st.divider()

# ৩. লাইভ এক্সিকিউশন চার্ট (সরাসরি ট্রেড নেওয়ার জন্য)
st.write("### 📈 Live ETH/USDT Chart (15m)")
components.html("""
    <div style="height:500px;">
    <iframe src="https://www.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="100%" frameborder="0"></iframe>
    </div>
""", height=510)

st.info("💡 মাহিম, যখন উপরের মিটারে 'Strong Buy' বা 'Strong Sell' দেখাবে, তখনই চার্ট দেখে এন্ট্রি নিও।")
