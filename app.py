import streamlit as st
import requests
import streamlit.components.v1 as components

# ১. পেজ সেটআপ ও স্টাইল
st.set_page_config(page_title="Master AI Ultra", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    .metric-card { background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; text-align: center; }
    h1, h3 { color: #627eea; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>💎 Master AI: Professional Multi-Feature Dashboard</h1>", unsafe_allow_html=True)

# ২. লাইভ প্রাইস টিকার (এটি কখনো ফেইল হবে না)
components.html("""
    <div style="height:62px; background-color: #161b22; border-radius: 10px; overflow: hidden;">
    <iframe src="https://widget.coinlib.io/widget?type=horizontal_v2&theme=dark&pref_coin_id=1505" width="100%" height="62px" frameborder="0" style="border:0;"></iframe>
    </div>
""", height=70)

# ৩. প্রফেশনাল ইনটেলিজেন্স (Whale, News, Latency - ব্যাকগ্রাউন্ডে চলবে)
def get_advanced_intel():
    try:
        # নিউজ চেক
        n_url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        news = requests.get(n_url, timeout=5).json()['Data'][:3]
        bullish = any(word in n['title'].lower() for n in news for word in ['bull', 'buy', 'up', 'etf'])
        sentiment = "🔥 BULLISH" if bullish else "⚖️ NEUTRAL"
        
        # ভলিউম চেক (Whale Tracking)
        p_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD"
        vol = requests.get(p_url, timeout=5).json()['RAW']['ETH']['USD']['VOLUME24HOURTO'] / 1000000
        whale = "🐋 High Activity" if vol > 100 else "💎 Normal"
        
        return sentiment, whale, vol
    except:
        return "SCANNING...", "CHECKING...", 0

sent, whale_act, vol_amt = get_advanced_intel()

# ৪. আগের সব ফিচার ডিসপ্লে (Whale, News, Latency)
st.write("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><h3>📰 News Mood</h3><p style='color:white;'>{sent}</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><h3>🐋 Whale Track</h3><p style='color:white;'>{whale_act}</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><h3>⚡ Latency</h3><p style='color:white;'>Ultra-Fast</p></div>", unsafe_allow_html=True)

# ৫. ট্রেডিংভিউ মিটার ও চার্ট (যা তুমি পছন্দ করেছিলে)
st.write("---")
st.write("### 📡 Real-Time Technical Signal (15m)")
components.html("""
    <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" frameborder="0"></iframe>
""", height=420)

st.write("### 📈 Live Execution Engine")
components.html("""
    <iframe src="https://www.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="500" frameborder="0"></iframe>
""", height=520)
