import streamlit as st
import streamlit.components.v1 as components

# ১. পেজ সেটআপ
st.set_page_config(page_title="Master AI Traffic Light", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    .signal-card {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: black;
        margin-bottom: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    h2, h3 { color: #f0b90b !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2>🚦 Master AI: Trade Traffic Light</h2>", unsafe_allow_html=True)

# ২. ডিসিশন মেকিং লজিক (Traffic Light)
st.write("### 🤖 Bot's Live Verdict")

# এখানে ৩টি ইনপুট নিচ্ছি যা বট অটোমেটিক চেক করার নির্দেশ দিবে
col_check1, col_check2, col_check3 = st.columns(3)
with col_check1:
    signal_strength = st.selectbox("Technical Meter কি বলছে?", ["Strong Buy", "Buy", "Neutral", "Sell"])
with col_check2:
    btc_status = st.selectbox("BTC এর অবস্থা কি?", ["Stable/Up", "Dropping Fast"])
with col_check3:
    news_impact = st.selectbox("কোনো লাল (High) নিউজ আছে?", ["No", "Yes"])

# ট্রাফিক লাইট লজিক
if signal_strength == "Strong Buy" and btc_status == "Stable/Up" and news_impact == "No":
    st.markdown('<div class="signal-card" style="background-color: #00ff88;">🟢 এখন ট্রেড নিন (SAFE TRADE)</div>', unsafe_allow_html=True)
    st.balloons()
elif (signal_strength == "Buy" or signal_strength == "Strong Buy") and (btc_status == "Dropping Fast" or news_impact == "Yes"):
    st.markdown('<div class="signal-card" style="background-color: #f0b90b;">🟡 অপেক্ষা করুন (DANGEROUS NEWS/BTC)</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="signal-card" style="background-color: #ff4b4b; color: white;">🔴 একদম ট্রেড নেবেন না (HIGH RISK)</div>', unsafe_allow_html=True)

st.divider()

# ৩. ভিজ্যুয়াল এনালাইসিস (প্রমাণ দেখার জন্য)
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 📡 Technical Analysis")
    components.html("""
        <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with col2:
    st.write("### 📅 Economic Calendar (News)")
    components.html("""
        <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&importanceFilter=1&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

st.divider()

# ৪. বিটকয়েন স্ট্যাবিলিটি চার্ট
st.write("### 📉 BTC Stability (বিটকয়েন নিচে পড়লে ট্রেড বাদ)")
components.html("""
    <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE%3ABTCUSDT&interval=15&theme=dark" width="100%" height="450" frameborder="0"></iframe>
""", height=460)
