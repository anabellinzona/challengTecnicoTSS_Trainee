import pandas as pd
import os

assets = ["MSFT", "GOOG", "AAPL", "TSLA"]

for asset in assets:

    filepath = f"data/{asset}.csv"
    print(f"Limpiando {asset}...")

    df = pd.read_csv(filepath)

    if "Date" in df.columns:
        pass

    else:
        df = pd.read_csv(filepath, index_col=0)
        df.reset_index(inplace=True)

        df.rename(columns={df.columns[0]: "Date"}, inplace=True)

    df = df[df["Date"] != "Ticker"]
    df = df[df["Date"] != "Date"]

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df = df.dropna(subset=["Date"])

    df = df.sort_values("Date")

    df.to_csv(filepath, index=False)

print("CSV limpiados correctamente.")
