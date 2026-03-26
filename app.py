import streamlit as st
import requests
import time
from streamlit_autorefresh import st_autorefresh

# ১. হাই-পারফরম্যান্স রিফ্রেশ
st.set_page_config(page_title="Master AI Ultra", layout="wide")
st_autorefresh(interval=30000, key="ultra_refresher")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    .signal-card {
        padding: 30px; border-radius: 20px; text-align: center;
        border: 2px solid #00d4ff; background: #161b22;
        box-shadow: 0px 4px 15px rgba(0, 212, 255, 0.3);
    }
    .metric-val { font-size: 24px; font-weight: bold; color: #f0b90b; }
    </style>
    """, unsafe_allow_html=True)

# ২. অ্যাডভান্সড এনালাইসিস ইঞ্জিন
def fetch_pro_data():
    try:
        # ETH ডাটা
        eth = requests.get("https://api.binance.com/api/3/ticker/24hr?symbol=ETHUSDT").json()
        price = float(eth['lastPrice'])
        change = float(eth['priceChangePercent'])
        volume = float(eth['quoteVolume']) / 1000000 # In Millions
        
        # ৩. স্মার্ট ফিল্টার লজিক (ভলিউম ১০০০ মিলিয়নের উপরে হলে স্ট্রং)
        verdict = "🛡️ SCANNING MARKET..."
        v_color = "#ffffff"
        
        if change > 0.8 and volume > 150:
            verdict = "🚀 STRONG BUY (CONFIRMED BY VOLUME)"
            v_color = "#00ff88"
        elif change < -2.0:
            verdict = "⚠️ STRONG SELL (DANGER ZONE)"
            v_color = "#ff4b4b"
        else:
            verdict = "⚖️ NEUTRAL (DO NOT ENTRY)"
            v_color = "#f0b90b"
            
        return price, change, volume, verdict, v_color
    except:
        return 0, 0, 0, "ERROR FETCHING DATA", "#ff4b4b"

p, c, v, verdict, col = fetch_pro_data()

# ৩. মেইন ডিসপ্লে
st.markdown(f"<h1 style='text-align: center; color: #627eea;'>💎 Master AI: Ultra-Accuracy Mode</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="signal-card" style="border-color: {col};">
        <h1 style="color: {col}; margin-bottom: 5px;">{verdict}</h1>
        <p style="color: #8b949e;">ETH Price: ${p} | 24h Change: {c}%</p>
    </div>
    """, unsafe_allow_html=True)

# ৪. প্রো ট্রেডিং মেট্রিক্স
st.write("---")
m1, m2, m3 = st.columns(3)
m1.metric("📊 24h Vol (USD)", f"${v:.2f}M")
m2.metric("📉 Price Status", f"{c}%")
m3.metric("⏱️ Timeframe", "15m (Fixed)")

# ৫. ওয়ার্ল্ড-ক্লাস চার্ট ও ইন্ডিকেটর
import streamlit.components.v1 as components
st.write("### 📈 Live Execution Engine")
components.html(f"""
    <iframe src="https://www.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="500" frameborder="0"></iframe>
""", height=510)
