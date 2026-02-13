import yfinance as yf

data = yf.download("MSFT", start="2021-01-01", end="2021-12-31")

if isinstance(data.columns, tuple) or hasattr(data.columns, 'levels'):
    data.columns = data.columns.get_level_values(0)

data.reset_index(inplace=True)

data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

data.to_csv("data/msft.csv", index=False)

print("Datos descargados correctamente.")
