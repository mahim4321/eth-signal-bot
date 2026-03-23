import streamlit as st

st.set_page_config(page_title="ETH High Accuracy", layout="wide")

st.markdown("<h2 style='text-align: center; color: #00ff88;'>🎯 ETH High-Accuracy Bot</h2>", unsafe_allow_html=True)

# ১. টেকনিক্যাল মিটার (Simple Version)
st.write("### 📡 Technical Analysis Signal")
html_meter = """
<iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?locale=en#%7B%22interval%22%3A%2215m%22%2C%22width%22%3A%22100%25%22%2C%22isTransparent%22%3Afalse%2C%22height%22%3A400%2C%22symbol%22%3A%22BINANCE%3AETHUSDT%22%2C%22showIntervalTabs%22%3Atrue%2C%22displayMode%22%3A%22single%22%2C%22colorTheme%22%3A%22dark%22%7D" 
width="100%" height="400" frameborder="0" style="border:none;"></iframe>
"""
st.components.v1.html(html_meter, height=410)

st.divider()

# ২. লাইভ চার্ট (Simple Version)
st.write("### 📈 Live ETH/USDT Chart")
html_chart = """
<iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_76296&symbol=BINANCE%3AETHUSDT&interval=15&hidesidetoolbar=1&hidetoptoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=dark&style=1&timezone=Etc%2FUTC&studies_overrides={}&overrides={}&enabled_features=[]&disabled_features=[]&locale=en&utm_source=localhost&utm_medium=widget&utm_campaign=chart&utm_term=BINANCE%3AETHUSDT" 
width="100%" height="500" frameborder="0" style="border:none;"></iframe>
"""
st.components.v1.html(html_chart, height=510)
