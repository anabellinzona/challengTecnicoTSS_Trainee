import pandas as pd
import os

assets = ["MSFT", "GOOG", "AAPL", "TSLA"]

for asset in assets:

    filepath = f"data/{asset}.csv"
    print(f"Limpiando {asset}...")

    # Leer sin asumir headers correctos
    df = pd.read_csv(filepath)

    # Si existe columna 'Date'
    if "Date" in df.columns:
        pass

    else:
        # Resetear índice si la fecha está ahí
        df = pd.read_csv(filepath, index_col=0)
        df.reset_index(inplace=True)

        # Renombrar primera columna a Date
        df.rename(columns={df.columns[0]: "Date"}, inplace=True)

    # Eliminar filas basura tipo 'Ticker'
    df = df[df["Date"] != "Ticker"]
    df = df[df["Date"] != "Date"]

    # Convertir fechas
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Eliminar filas inválidas
    df = df.dropna(subset=["Date"])

    # Ordenar
    df = df.sort_values("Date")

    # Guardar limpio
    df.to_csv(filepath, index=False)

print("CSV limpiados correctamente.")
