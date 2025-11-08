import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import datetime
import os

# --- Connect to PostgreSQL ---
DB_CONFIG = {
    "user": "postgres",
    "password": "12345",
    "host": "localhost",
    "port": "5432",
    "database": "crypto_pipeline"
}

connection_string = (
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

engine = create_engine(connection_string)

# --- Load Data ---
query = "SELECT * FROM crypto_prices;"
df = pd.read_sql(query, engine)

# --- Create Output Folder ---
os.makedirs("outputs", exist_ok=True)

# --- Visualization ---
plt.figure(figsize=(10,6))
top_coins = df.nlargest(5, 'market_cap')

plt.bar(top_coins['symbol'], top_coins['market_cap'], color='gold')
plt.title("Top 5 Cryptocurrencies by Market Cap")
plt.xlabel("Symbol")
plt.ylabel("Market Cap (USD)")
plt.grid(axis='y', alpha=0.3)

# --- Save Chart with Timestamp ---
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
chart_path = f"outputs/crypto_marketcap_{timestamp}.png"
plt.tight_layout()
plt.savefig(chart_path)

print(f"Chart saved successfully to {chart_path}")
