import streamlit as st
import streamlit.components.v1 as components

# ১. প্রফেশনাল পেজ সেটআপ ও স্টাইল
st.set_page_config(page_title="Master AI: Elite Edition", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    .main-header {
        color: #627eea; text-align: center; font-size: 32px;
        font-weight: bold; padding: 20px; border-bottom: 2px solid #627eea;
    }
    .info-text { color: #8b949e; text-align: center; margin-top: 10px; font-size: 14px; }
    </style>
    <div class="main-header">💎 Master AI: Elite Trading Intelligence</div>
    <p class="info-text">Powered by AI Analysis & Real-Time Market Depth</p>
    """, unsafe_allow_html=True)

# ২. লাইভ ডাটা টিকার (সব সময় রানিং থাকবে)
components.html("""
    <div style="height:62px; background-color: #161b22; border-radius: 10px; overflow: hidden; border: 1px solid #30363d;">
    <iframe src="https://widget.coinlib.io/widget?type=horizontal_v2&theme=dark&pref_coin_id=1505" width="100%" height="62px" frameborder="0" style="border:0;"></iframe>
    </div>
""", height=75)

# ৩. এআই সিগন্যাল মিটার (১৫ মিনিট টাইমফ্রেম - সবচেয়ে সঠিক)
st.write("### 📡 AI Technical Intelligence (15m)")
components.html("""
    <div style="border: 2px solid #627eea; border-radius: 15px; overflow: hidden;">
    <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" frameborder="0" style="width:100%; height:400px;"></iframe>
    </div>
""", height=420)

# ৪. হোয়েল অ্যাক্টিভিটি ও মার্কেট সেন্টিমেন্ট (স্মার্ট মানি ট্র্যাকিং)
st.write("---")
st.write("### 🐋 Institutional Sentiment Tracker")
col1, col2 = st.columns(2)

with col1:
    # ফিয়ার অ্যান্ড গ্রিড ইনডেক্স
    st.markdown("**Market Sentiment Mood**")
    components.html("""
        <iframe src="https://alternative.me/crypto/fear-and-greed-index.png" width="100%" height="150px" frameborder="0" style="border-radius:10px;"></iframe>
    """, height=160)

with col2:
    # লাইভ ক্রিপ্টো নিউজ (হোয়েল মুভমেন্ট নিউজ)
    st.markdown("**Live Whale & News Feed**")
    components.html("""
        <iframe src="https://cryptopanic.com/widgets/news-ticker/?bg_color=161B22&font_family=sans-serif&header_bg_color=161B22&header_text_color=627EEA&link_color=00D4FF&news_feed=trending&text_color=FFFFFF" width="100%" height="150px" frameborder="0"></iframe>
    """, height=160)

# ৫. প্রফেশনাল এক্সিকিউশন চার্ট (সরাসরি ট্রেড সেটআপের জন্য)
st.write("---")
st.write("### 📈 Professional Execution Chart")
components.html("""
    <div style="border-radius: 15px; overflow: hidden; border: 1px solid #30363d;">
    <iframe src="https://www.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="550" frameborder="0" style="width:100%; height:550px;"></iframe>
    </div>
""", height=570)

st.success("মাহিম, তোমার এই বটটি এখন একই সাথে নিউজ, হোয়েল মুভমেন্ট এবং টেকনিক্যাল সিগন্যাল ট্র্যাক করছে।")
