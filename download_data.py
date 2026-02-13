import yfinance as yf
import os

assets = ["MSFT", "GOOG", "AAPL", "TSLA"]

os.makedirs("data", exist_ok=True)

for asset in assets:
    print(f"Descargando {asset}...")

    data = yf.download(
        asset,
        start="2021-01-01",
        end="2021-12-31",
        interval="1d"
    )

    filepath = f"data/{asset}.csv"
    data.to_csv(filepath)

    print(f"Guardado en {filepath}")

print("Descarga completa.")
