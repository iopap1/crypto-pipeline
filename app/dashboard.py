# app/dashboard.py
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Basic page config
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

@st.cache_data(show_spinner=False)
def load_latest_csv(data_dir: str) -> pd.DataFrame | None:
    """Return the most recent crypto_data_*.csv as a DataFrame, or None if not found."""
    pattern = os.path.join(data_dir, "crypto_data_*.csv")
    files = glob.glob(pattern)
    if not files:
        return None
    # Filenames include timestamp; sort by filename descending to get the newest
    latest = sorted(files, reverse=True)[0]
    df = pd.read_csv(latest)
    # Normalize expected columns if needed
    expected = {"id", "symbol", "current_price", "market_cap", "total_volume"}
    missing = expected - set(df.columns)
    if missing:
        st.warning(f"File {os.path.basename(latest)} is missing columns: {', '.join(sorted(missing))}")
    return df

st.title("Cryptocurrency Dashboard")

# Load data
df = load_latest_csv(DATA_DIR)

if df is None or df.empty:
    st.error("No data found in /data. Run the ETL pipeline to create a new CSV (crypto_data_*.csv).")
    st.stop()

# Sidebar controls
st.sidebar.header("Filters")
top_n = st.sidebar.slider("Top N by market cap", min_value=3, max_value=20, value=10, step=1)

# Basic table preview
st.subheader("Latest Snapshot")
st.caption("Showing the most recent file under /data matching crypto_data_*.csv")
st.dataframe(df, use_container_width=True)

# Ensure required columns exist
required_cols = ["id", "symbol", "current_price", "market_cap", "total_volume"]
for c in required_cols:
    if c not in df.columns:
        st.error(f"Column '{c}' not found in the dataset.")
        st.stop()

# Compute top N by market cap
top_df = df.nlargest(top_n, "market_cap")[["id", "symbol", "current_price", "market_cap", "total_volume"]]

# Metrics for a selected coin
st.subheader("Coin Detail")
coin = st.selectbox("Select a coin", top_df["id"].tolist())
sel = df[df["id"] == coin].head(1)

col1, col2, col3 = st.columns(3)
if not sel.empty:
    col1.metric("Price (USD)", f"{sel['current_price'].iloc[0]:,.2f}")
    col2.metric("Market Cap (USD)", f"{sel['market_cap'].iloc[0]:,.0f}")
    col3.metric("24h Volume (USD)", f"{sel['total_volume'].iloc[0]:,.0f}")

# Charts
st.subheader(f"Top {top_n} by Market Cap")

# Market cap bar chart
fig1, ax1 = plt.subplots()
ax1.bar(top_df["symbol"], top_df["market_cap"])
ax1.set_xlabel("Symbol")
ax1.set_ylabel("Market Cap (USD)")
ax1.set_title(f"Top {top_n} Cryptocurrencies by Market Cap")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig1, clear_figure=True)

# Volume bar chart
st.subheader(f"Top {top_n} by 24h Volume")
fig2, ax2 = plt.subplots()
ax2.bar(top_df["symbol"], top_df["total_volume"])
ax2.set_xlabel("Symbol")
ax2.set_ylabel("24h Volume (USD)")
ax2.set_title(f"Top {top_n} Cryptocurrencies by 24h Volume")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig2, clear_figure=True)

st.info(
    "Tip: schedule the ETL pipeline to run periodically so this dashboard always reflects fresh data. "
    "The app reads the latest CSV from /data."
)
