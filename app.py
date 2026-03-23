import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ETH 90% Accuracy Bot", layout="wide")

st.markdown("<h1 style='text-align: center; color: #00ff88;'>🎯 ETH High-Accuracy Trading Bot</h1>", unsafe_allow_html=True)

# কলাম সেটআপ
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📍 Technical Summary (Check 15m & 1h)")
    # ১৫ মিনিট এবং ১ ঘণ্টার সিগন্যাল একসাথে দেখার জন্য
    components.html(
        """
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
          {
          "interval": "15m",
          "width": "100%",
          "height": 410,
          "symbol": "BINANCE:ETHUSDT",
          "showIntervalTabs": true,
          "displayMode": "single",
          "locale": "en",
          "colorTheme": "dark"
          }
          </script>
        </div>
        """, height=430
    )

with col2:
    st.subheader("📈 Market Screener (Confirmation)")
    # ভলিউম এবং ট্রেন্ড কনফার্ম করার জন্য স্ক্রিনার
    components.html(
        """
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-hotlists.js" async>
          {
          "colorTheme": "dark",
          "dateRange": "12M",
          "exchange": "crypto",
          "showChart": true,
          "locale": "en",
          "width": "100%",
          "height": 410,
          "largeChartHeight": 312,
          "isTransparent": false,
          "showSymbolLogo": true
          }
          </script>
        </div>
        """, height=430
    )

st.divider()

# প্রো চার্ট উইথ অটো-পিভট এবং ভলিউম
st.subheader("🔍 Advanced Analysis (Volume & Pivot)")
components.html(
    """
    <div class="tradingview-widget-container" style="height:600px">
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
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "withdateranges": true,
      "hide_side_toolbar": false,
      "allow_symbol_change": true,
      "watchlist": ["BINANCE:BTCUSDT", "BINANCE:ETHUSDT"],
      "details": true,
      "hotlist": true,
      "calendar": true,
      "studies": [
        "RSI@tv-basicstudies",
        "Volume@tv-basicstudies",
        "MASimple@tv-basicstudies"
      ],
      "container_id": "tradingview_chart"
    }
      );
      </script>
    </div>
    """, height=620
)
