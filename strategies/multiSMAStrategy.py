import backtrader as bt;

class MultiSMAStrategy(bt.Strategy):

    def __init__(self):
        
        self.sma10 = bt.indicators.SMA(self.data.close, period = 10) #calcula el promedio del precio en los últimos 10 días
        self.sma30 = bt.indicators.SMA(self.data.close, period = 30) #calcula el promedio del precio en los últimos 30 días

        self.crossover = bt.indicators.CrossOver(self.sma10, self.sma30)

        self.positionByStrategy = { #básicamente es un contador que registra quién compró qué
            "sma10": 0,
            "sma30": 0,
            "golden": 0
        }

        self.trades_log = [] #guarda cada compra/venta
        self.portfolio_values = [] #guarda el portfolio por día
    
    def next(self):

        portfolio_value = self.broker.getvalue()
        self.portfolio_values.append({
            "date": self.datas[0].datetime.date(0),
            "value": portfolio_value
        })

        #ESTRATÉGIA SMA10
        if self.data.close[0] > self.sma10[0]: #el precio de hoy, está por encima del promedio de precios de los últimos 10 días?
            if self.positionByStrategy["sma10"] == 0: #si aún no compró
                
                portfolio_value = self.broker.getvalue() #el valor entero
                amount_to_invest = portfolio_value * 0.10 #lo que invierte
                price = self.data.close[0]
                size = int(amount_to_invest / price) #cuántas acciones compró

                cash = self.broker.getcash()

                if cash >= amount_to_invest and size > 0:
                    print(f"BUY: {self.data.close[0]}", size)
                    self.buy(size = size)
                    self.positionByStrategy["sma10"] += size #le asigno que ya compró

                    self.trades_log.append({
                        "date": self.datas[0].datetime.date(0),
                        "strategy": "SMA10",
                        "action": "BUY",
                        "price": price,
                        "size": size
                    })

        elif self.data.close[0] < self.sma10[0]: #el precio de hoy, está por debajo del promedio de precios de los últimos 10 días?
            if self.positionByStrategy["sma10"] > 0: #la estrategia SMA10 tiene algo comprador?
                
                size = self.positionByStrategy["sma10"]

                print(f"SELL: {self.data.close[0]}", size) #vendo
                
                self.sell(size = size)
                
                self.positionByStrategy["sma10"] = 0

                self.trades_log.append({
                    "date": self.datas[0].datetime.date(0),
                    "strategy": "SMA10",
                    "action": "SELL",
                    "price": self.data.close[0],
                    "size": size
                })
        


        #ESTRATÉGICA SMA30
        if self.data.close[0] > self.sma30[0]:
            if self.positionByStrategy["sma30"] == 0:

                portfolio_value = self.broker.getvalue()
                amount_to_invest = portfolio_value * 0.10
                price = self.data.close[0]
                size = int(amount_to_invest / price)

                cash = self.broker.getcash()

                if cash >= amount_to_invest and size > 0:
                    print(f"BUY: {self.data.close[0]}", size)
                    self.buy(size = size)
                    self.positionByStrategy["sma30"] += size

                    self.trades_log.append({
                        "date": self.datas[0].datetime.date(0),
                        "strategy": "SMA30",
                        "action": "BUY",
                        "price": price,
                        "size": size
                    })


        elif self.data.close[0] < self.sma30[0]:
            if self.positionByStrategy["sma30"] > 0:
                size = self.positionByStrategy["sma30"]

                print(f"SELL: {self.data.close[0]}", size)
                self.sell(size = size)
                self.positionByStrategy["sma30"] = 0

                self.trades_log.append({
                    "date": self.datas[0].datetime.date(0),
                    "strategy": "SMA30",
                    "action": "SELL",
                    "price": self.data.close[0],
                    "size": size
                })


        #ESTRATEGIA GOLDEN
        if self.crossover > 0:
            if self.positionByStrategy["golden"] == 0:

                portfolio_value = self.broker.getvalue()
                amount_to_invest = portfolio_value * 0.10
                price = self.data.close[0]
                size = int(amount_to_invest / price)

                cash = self.broker.getcash()

                if cash >= amount_to_invest and size > 0:
                    print(f"BUY: {self.data.close[0]}", size)
                    self.buy(size = size)
                    self.positionByStrategy["golden"] += size

                    self.trades_log.append({
                        "date": self.datas[0].datetime.date(0),
                        "strategy": "GOLDEN",
                        "action": "BUY",
                        "price": price,
                        "size": size
                    })


        elif self.crossover < 0:
            if self.positionByStrategy["golden"] > 0:

                size = self.positionByStrategy["golden"]

                print(f"SELL: {self.data.close[0]}", size)
                self.sell(size = size)
                self.positionByStrategy["golden"] = 0

                self.trades_log.append({
                    "date": self.datas[0].datetime.date(0),
                    "strategy": "GOLDEN",
                    "action": "SELL",
                    "price": self.data.close[0],
                    "size": size
                })
        #solo COMPRA si NO TIENE nada y solo VENDE SI TIENE algo
    
    def stop(self):
        print("TRASACTIONS")

        for trade in self.trades_log:
            print(trade)
        
        print("PORTFOLIO VALUE")

        for value in self.portfolio_values[-5:]:
            print(value)