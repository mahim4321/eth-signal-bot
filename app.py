import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh

# ১. পেজ সেটআপ ও অটো-রিফ্রেশ (প্রতি ৩০ সেকেন্ডে আপডেট হবে)
st.set_page_config(page_title="Master AI Ultra", layout="wide")
st_autorefresh(interval=30000, key="master_refresher")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    .signal-box {
        padding: 25px; border-radius: 15px; text-align: center;
        border: 2px solid #627eea; background: #161b22;
        box-shadow: 0px 4px 15px rgba(98, 126, 234, 0.2);
    }
    .metric-card { background: #0b0e11; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# ২. প্রফেশনাল ডাটা ও সেন্টিমেন্ট ইঞ্জিন
def fetch_master_intel():
    try:
        # মেইন প্রাইস ডাটা
        price_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD"
        p_resp = requests.get(price_url, timeout=10).json()
        eth_data = p_resp['RAW']['ETH']['USD']
        
        price = eth_data['PRICE']
        change = eth_data['CHANGEPCT24HOUR']
        volume = eth_data['VOLUME24HOURTO'] / 1000000
        
        # নিউজ সেন্টিমেন্ট (NLP Logic)
        news_url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        n_resp = requests.get(news_url).json()
        headlines = [n['title'].lower() for n in n_resp['Data'][:5]]
        bullish_words = ['bullish', 'launch', 'upgrade', 'etf', 'buy', 'high', 'partnership']
        score = sum(1 for h in headlines if any(w in h for w in bullish_words))
        
        sentiment = "🔥 BULLISH" if score >= 1 else "⚖️ NEUTRAL"
        
        # সিগন্যাল লজিক
        if change > 0.5 and score >= 1:
            verdict, v_color = "🚀 STRONG BUY", "#00ff88"
        elif change < -1.5:
            verdict, v_color = "⚠️ DANGER / SELL", "#ff4b4b"
        else:
            verdict, v_color = "⚖️ HOLD / WAIT", "#f0b90b"
            
        return price, change, volume, sentiment, verdict, v_color
    except:
        return 0, 0, 0, "SCANNING...", "CONNECTING...", "#ffffff"

p, c, v, sent, verd, col = fetch_master_intel()

# ৩. মেইন ড্যাশবোর্ড ডিসপ্লে
st.markdown("<h1 style='text-align: center; color: #627eea;'>💎 Master AI: Professional Dashboard</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="signal-box" style="border-color: {col};">
        <h1 style="color: {col};">{verd}</h1>
        <p style="color: #8b949e; font-size: 20px;">News Sentiment: <b>{sent}</b></p>
        <h2 style="color: #f0b90b;">ETH Price: ${p:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

# ৪. হোয়েল ট্র্যাকিং ও ল্যাটেন্সি গার্ড
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("📊 24h Volume", f"${v:.2f}M")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("📉 Price Change", f"{c:.2f}%")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.write("**🐋 Whale Activity**")
    st.write("High Volume Detected" if v > 100 else "Normal Activity")
    st.markdown("</div>", unsafe_allow_html=True)

# ৫. প্রফেশনাল চার্ট ও টেকনিক্যাল মিটার
st.write("### 📈 Live Execution Chart (15m)")
components.html("""
    <iframe src="https://www.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="500" frameborder="0"></iframe>
""", height=510)

st.write("### 📡 Technical Strength Meter")
components.html("""
    <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" frameborder="0"></iframe>
""", height=410)
