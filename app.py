import streamlit as st
import streamlit.components.v1 as components

# ১. পেজ সেটআপ এবং গোল্ডেন থিম
st.set_page_config(page_title="ETH Pro Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    h1, h3 { color: #f0b90b !important; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1e2329; 
        border-radius: 5px; 
        color: white; 
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ETH Professional Trader Suite")

# ২. ট্যাব সিস্টেম (যাতে মোবাইলে অগোছালো না লাগে)
tab1, tab2, tab3 = st.tabs(["📊 Live Analysis", "🌍 Market News", "📝 Trade Journal"])

with tab1:
    st.write("### ⚡ Real-Time ETH Signal")
    # বিন্যান্স প্রাইস বার
    components.html("""
        <iframe src="https://s.tradingview.com/embed-widget/symbol-info/?symbol=BINANCE%3AETHUSDT&colorTheme=dark" width="100%" height="150" frameborder="0"></iframe>
    """, height=160)
    
    # সিগন্যাল মিটার
    components.html("""
        <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE%3AETHUSDT&interval=15m&colorTheme=dark&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
    """, height=410)
    
    st.divider()
    
    # প্রো চার্ট
    st.write("### 📈 Advanced Chart")
    components.html("""
        <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE%3AETHUSDT&interval=15&theme=dark" width="100%" height="500" frameborder="0"></iframe>
    """, height=520)

with tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 📅 Economic Events")
        components.html("""
            <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
        """, height=420)
    with col_b:
        st.write("### 🌍 Fear & Greed")
        st.image("https://alternative.me/crypto/fear-and-greed-index.png", use_container_width=True)

with tab3:
    st.write("### 📝 Trading Journal")
    journal_note = st.text_area("আপনার আজকের ট্রেড প্ল্যান লিখুন...", height=200)
    if st.button("Save Entry"):
        st.success("নোটটি সফলভাবে সংরক্ষিত হয়েছে!")
