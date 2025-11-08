import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# PostgreSQL connection
DB_USER = "postgres"
DB_PASSWORD = "12345"  # change this
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_pipeline"

# Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Query the table
query = "SELECT symbol, current_price, market_cap, total_volume FROM crypto_prices;"
df = pd.read_sql(query, engine)

# Display info
print("✅ Data loaded from PostgreSQL!")
print(df.head())

# Plot market caps
plt.figure(figsize=(10,6))
plt.bar(df['symbol'], df['market_cap'], color='limegreen')
plt.title("Top 10 Cryptocurrencies by Market Cap")
plt.xlabel("Symbol")
plt.ylabel("Market Cap (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
