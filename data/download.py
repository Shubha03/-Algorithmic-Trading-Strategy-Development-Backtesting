import yfinance as yf
import os
import pandas as pd

os.makedirs("data", exist_ok=True)

ticker = "AAPL"

df = yf.download(
    ticker,
    start="2018-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Flatten multi-index columns if they exist
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)


df.to_csv(f"data/{ticker}.csv")