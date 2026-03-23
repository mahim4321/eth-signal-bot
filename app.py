import streamlit as st
import streamlit.components.v1 as components

# একদম হালকা পেজ সেটআপ
st.set_page_config(page_title="ETH High Accuracy", layout="wide")

st.markdown("<h2 style='text-align: center; color: #00ff88;'>🎯 ETH High-Accuracy Bot</h2>", unsafe_allow_html=True)

# ১. টেকনিক্যাল মিটার (সরাসরি মেইন বডিতে)
st.write("### 📡 Technical Analysis Signal")
components.html(
    """
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
      {
      "interval": "15m",
      "width": "100%",
      "height": 450,
      "symbol": "BINANCE:ETHUSDT",
      "showIntervalTabs": true,
      "displayMode": "single",
      "locale": "en",
      "colorTheme": "dark"
    }
      </script>
    </div>
    """,
    height=480,
)

st.divider()

# ২. লাইভ চার্ট (সরাসরি মেইন বডিতে)
st.write("### 📈 Live ETH/USDT Chart")
components.html(
    """
    <div class="tradingview-widget-container" style="height:500px">
      <div id="tradingview_chart"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "autosize": true,
      "symbol": "BINANCE:ETHUSDT",
      "interval": "15",
      "timezone": "Etc/UTC",
      "theme": "dark",
      "style": "1",
      "locale": "en",
      "enable_publishing": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_chart"
    }
      );
      </script>
    </div>
    """,
    height=520,
)
