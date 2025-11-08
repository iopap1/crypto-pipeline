import pandas as pd
from sqlalchemy import create_engine
import os

DB_CONFIG = {
    "user": "postgres",
    "password": "12345",  # change if needed
    "host": "localhost",
    "port": "5432",
    "database": "crypto_pipeline"
}

def load_to_postgres():
    """Loads cleaned crypto data into PostgreSQL"""
    file_path = "../db/clean_crypto_data.csv"

    if not os.path.exists(file_path):
        print("Clean data file not found. Run transform step first.")
        return

    df = pd.read_csv(file_path)
    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    df.to_sql("crypto_prices", engine, if_exists="replace", index=False)
    print("Data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    load_to_postgres()
