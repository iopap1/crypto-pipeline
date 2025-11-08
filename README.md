# 🚀 Cryptocurrency Data Pipeline Project

### 📊 Automated ETL + Visualization with Python & PostgreSQL

This project is an **end-to-end data pipeline** that automatically:
1. **Extracts** live cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api).
2. **Transforms** and cleans the data for analysis.
3. **Loads** it into a **PostgreSQL** database for storage.
4. **Visualizes** insights — like the *Top 5 cryptocurrencies by market capitalization* — using **Matplotlib**.

---

## 🧠 Project Overview

This project showcases:
- Real-time data ingestion from an API  
- ETL pipeline development with modular scripts  
- Database integration (PostgreSQL + SQLAlchemy)  
- Data analysis and visualization using Python  
- Logging, automation, and maintainable structure

---

## 📊 Dashboard Preview

Here’s a look at the interactive Streamlit dashboard included in this project.

**Dashboard Snapshot**
![Crypto Dashboard Table](assets/crypto_dashboard_table.png)

**Market Cap Visualization**
![Crypto Dashboard Chart](assets/crypto_dashboard_chart.png)

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python 3.12 |
| **Database** | PostgreSQL |
| **Libraries** | `pandas`, `requests`, `sqlalchemy`, `matplotlib` |
| **Tools** | VS Code, pgAdmin, Windows Task Scheduler |

---

## 🧩 Project Structure

crypto-pipeline/
│
├── etl/
│ ├── fetch.py # Extracts live crypto data from CoinGecko
│ ├── transform.py # Cleans and prepares data
│ ├── load.py # Loads data into PostgreSQL
│
├── app/
│   └── dashboard.py          # Streamlit dashboard
├── data/ # Stores raw data files (CSV)
├── db/ # Stores cleaned data
├── outputs/ # Stores generated charts
│
├── visualize.py # Creates charts and insights
├── run_pipeline.py # Automates full ETL process
├── pipeline_log.txt # Log of each run
└── README.md # Project documentation

---

## 🧠 How It Works

1. **Fetch Data**  
   Calls the CoinGecko API and retrieves the top 10 cryptocurrencies.

2. **Transform Data**  
   Cleans the dataset, removes duplicates, and standardizes values.

3. **Load Data**  
   Inserts clean data into a PostgreSQL database (`crypto_prices` table).

4. **Visualize**  
   Generates bar charts showing top 5 coins by market cap.

---

## 🖥️ Run the Project Locally

1. **Clone the repository**
git clone https://github.com/iopap1/crypto-pipeline.git
cd crypto-pipeline


2. **Create a virtual environment**
python -m venv venv
venv\Scripts\activate


3. **Ιnstall dependencies**
pip install pandas requests matplotlib sqlalchemy psycopg2-binary


4. **Run the full pipeline**
python run_pipeline.py


5. **Check Output**

- Clean CSV: db/clean_crypto_data.csv
- Visualization: outputs/crypto_marketcap_<timestamp>.png
- Database Table: crypto_prices in PostgreSQL


6. **Run the Dashboard (Streamlit)**

The Streamlit dashboard lets you explore the latest cryptocurrency data interactively.  
It reads the most recent CSV saved in the `data/` folder (created by the ETL pipeline).

### 1. Install requirements (only once)
```bash
pip install -r requirements.txt

### 2. Run the Streamlit app
cd app
streamlit run dashboard.py

Then open your browser at:
http://localhost:8501

You can:

- Adjust the number of coins displayed with the “Top N by market cap” slider

- View key metrics (price, market cap, trading volume) for each coin

- Explore live data fetched from the CoinGecko API


