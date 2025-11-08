import pandas as pd
import os

def transform_crypto_data():
    """
    Cleans and transforms the most recent crypto data CSV.
    """
    data_dir = "../data"
    db_dir = "../db"
    os.makedirs(db_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(data_dir) if f.startswith("crypto_data_")])
    if not files:
        print("No data files found to transform.")
        return

    latest_file = os.path.join(data_dir, files[-1])
    df = pd.read_csv(latest_file)

    # Remove duplicates, handle missing data
    df = df.drop_duplicates()
    df = df.dropna(subset=["id", "symbol", "current_price"])

    # Convert price to float
    df["current_price"] = df["current_price"].astype(float)

    # Save cleaned data
    clean_path = os.path.join(db_dir, "clean_crypto_data.csv")
    df.to_csv(clean_path, index=False)
    print(f"Cleaned data saved to {clean_path}")

if __name__ == "__main__":
    transform_crypto_data()
