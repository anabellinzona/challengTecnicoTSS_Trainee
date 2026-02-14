# Trading Strategy Challenge - Backtrader

## Descripción general

En este proyecto se implementó una estrategia de trading multi-activo utilizando el framework Backtrader en Python.
La estrategia opera sobre distintos instrumentos financieros aplicando señales basadas en Simple Moving Averages (SMA), ejecutando órdenes de compra y venta durante el período 2021.
El sistema simula la evolución de un portfolio con un capital inicial de 100.000 USD.

## Estrategia implementada

### Se llevaron a cabo tres estrategias independientes:
1. SMA10
   * Compra: cuando el precio cruza por encima de la SMA de 10 días
   * Venta: cuando el precio cae por debajo de la SMA de 10 días.
2. SMA30
   * Compra: cuando el precio cruza por encima de la SMA de 30 días
   * Venta: cuando el precio cae por debajo de la SMA de 30 días.
3. GOLDEN
    * Compra: cuando la SMA de 10 días cruza por encima de la SMA de 30 días
    * Venta: cuando la SMA de 30 días cruza por encima de la SMA de 10 días
  
## Reglas de estratégia

### Para poder resolver esto se debió tener en cuenta diferentes restricciones:

* Cada posición solo puede cerrarse con la misma estrategia que la abrió.
* Se permiten múltiples compras del mismo activo.
* Cada compra invierte el 10% del valor total del portfolio al momento de la señal.
* Si no hay liquidez suficiente, la orden no se ejecuta.
* No se permite short selling.
* No se venden activos que no estén.

## Activos analizados
### La simulación se ejecutó sobre:
* MSFT (Microsoft)
* GOOG (Google)
* APPL (Apple)
* TSLA (Tesla)
Teniendo en cuenta los datos correspondientes al 2021

## Estructura del proyecto

Para este proyecto se desarrolló la siguiente estructura:

ChallengeTecnicoTSS_Trainee

```
challengeTecnicoTSS_Trainee/ 
│ 
├── data/ # CSV originales descargados de Yahoo Finance 
| └── AAPL
| └── MSFT
| └── GOOG
| └── TSLA
├── strategies/ # Implementación de estrategias de trading 
│ └── multiSMAStrategy.py 
├── clean_data.py # Script para limpieza y formateo de datos 
├── main.py # Script principal que ejecuta el backtest 
├── requirements.txt # Dependencias del proyecto 
└── README.md # Documentación del challenge
```

## Resultados generados
### Al finalizar la ejecución se muestran los resultados finales:
1. Registro de Transacciones
   
   Ejemplo: Date: 2021-02-07 | Strategy: SMA10 | Action: BUY | Price: 234.86 | Size: 42

   Este modelo incluye:
   - Fecha
   - Estratégia (SMA10, SMA30, GOLDEN)
   - Acción (BUY, SELL)
   - Precio
   - Tamaño
2. Evolución del Portfolio
   
   Ejemplo: Date: 2021-12-23 | Value: 115876.06
   
   Esta evolución permite analizar la valuación a lo largo del tiempo
4. Resultado Final
   
   - Portfolio Inicial: 100000 USD
   - Portfolio Final: 116187.25 USD
   - Ganancia: 16187.25 USD
   - Retorno: 16.19%

## Funcionalidades destacadas

- Backtesting multi-activo
- Estrategias independientes por señal
- Position sizing dinámico
- Validación de liquidez
- Registro de operaciones
- Seguimiento del valor del portfolio

## Posibles Mejoras

- Gráfico de equity curve
- Cálculo de Sharpe Ratio
- Maximum Drawdown
- Comparación vs Buy & Hold
- Costos de transacción

