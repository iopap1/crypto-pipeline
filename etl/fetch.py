import requests
import pandas as pd
from datetime import datetime
import os

# Define where to save the data
DATA_DIR = "../data"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_crypto_data():
    """
    Fetches real-time cryptocurrency market data from CoinGecko API.
    Saves it as a CSV file in the /data folder.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,  # fetch top 10 coins
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # Keep only useful columns
        df = df[["id", "symbol", "current_price", "market_cap", "total_volume"]]

        # Add a timestamp for reference
        df["fetched_at"] = datetime.utcnow()

        # Define file path
        file_path = os.path.join(DATA_DIR, f"crypto_data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv")

        # Save to CSV
        df.to_csv(file_path, index=False)
        print(f"Data fetched and saved successfully: {file_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_crypto_data()
