import backtrader as bt;
import os, csv

class MultiSMAStrategy(bt.Strategy):

    def __init__(self):

        self.sma10 = {}
        self.sma30 = {}
        self.crossover = {}

        self.positionByStrategy = {}

        self.trades_log = [] 
        self.portfolio_values = [] 

        for data in self.datas:
            self.sma10 = bt.indicators.SMA(data.close, period = 10)
            self.sma30 = bt.indicators.SMA(data.close, period = 30)

            self.crossover[data] = bt.indicators.CrossOver(
                self.sma10[data],
                self.sma30[data]
            )

            self.positionByStrategy[data] = { 
                "sma10": 0,
                "sma30": 0,
                "golden": 0
            }
    
    def next(self):

        portfolio_value = self.broker.getvalue()
        self.portfolio_values.append({
            "date": self.datas[0].datetime.date(0),
            "value": portfolio_value
        })

        #ESTRATÉGIA SMA10
        if self.data.close[0] > self.sma10[0]: 
            if self.positionByStrategy["sma10"] == 0: 
                
                portfolio_value = self.broker.getvalue() 
                amount_to_invest = portfolio_value * 0.10 
                price = self.data.close[0]
                size = int(amount_to_invest / price) 

                cash = self.broker.getcash()

                if cash >= amount_to_invest and size > 0:
                    self.buy(size = size)
                    self.positionByStrategy["sma10"] += size

                    self.trades_log.append({
                        "date": self.datas[0].datetime.date(0),
                        "strategy": "SMA10",
                        "action": "BUY",
                        "price": price,
                        "size": size
                    })

        elif self.data.close[0] < self.sma10[0]:
            if self.positionByStrategy["sma10"] > 0: 
                
                size = self.positionByStrategy["sma10"]
                
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
        print("="*40)
        print("TRASACTIONS") 
        print("="*40)

        for trade in self.trades_log:
            print( f"Date: {trade['date']} | "
                  f"Strategy: {trade['strategy']} | "
                  f"Action: {trade["action"]} | "
                  f"Price: {round(trade["price"], 2)} | "
                  f"Size: {trade["size"]} |")
        
        print("="*40)
        print("PORTFOLIO VALUE")
        print("="*40)

        for value in self.portfolio_values[-5:]:
            print(f"Date: {value['date']} | "
                  f"Value: {round(value['value'], 2)}")
        
        final_value = self.broker.getvalue()
        initial_value = 100000
        profit = final_value - initial_value
        return_pct = (profit / initial_value) * 100

        print("="*40)
        print("FINAL RESULT")
        print("="*40)

        print(f"Initial Portfolio: {initial_value}")
        print(f"Final Portfolio: {final_value}")
        print(f"Profit: {profit}")
        print(f"Return %: {round(return_pct, 2)}%")

        os.makedirs("outputs", exist_ok=True)

        with open("outputs/trades.csv", "w", newline="") as file:

            write = csv.writer(file)

            write.writerow(["date", "strategy", "action", "price", "size"])

            for trade in self.trades_log:
                write.writerow([
                    trade["date"],
                    trade["strategy"],
                    trade["action"],
                    trade["price"],
                    trade["size"]
                ])
        
        with open("outputs/portfolio.csv", "w", newline="") as file:
            write = csv.writer(file)

            write.writerow(["date", "value"])

            for value in self.portfolio_values:
                write.writerow([
                    value["date"],
                    value["value"]
                ])
