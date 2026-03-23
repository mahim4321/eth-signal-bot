import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ETH Pro Signal", layout="wide")

st.title("📊 ETH Real-Time Pro Dashboard")

# TradingView Technical Analysis Widget
st.subheader("Technical Analysis Signal")
components.html(
    """
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
      {
      "interval": "15m",
      "width": "100%",
      "isTransparent": false,
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

# TradingView Live Chart Widget
st.subheader("Live ETH/USDT Chart")
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
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "hide_side_toolbar": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_chart"
    }
      );
      </script>
    </div>
    """,
    height=520,
)

st.write("Last Sync:", st.session_state.get('last_sync', 'Live Now'))
