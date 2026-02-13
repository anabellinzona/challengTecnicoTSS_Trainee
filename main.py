import backtrader as bt
from strategies.multiSMAStrategy import MultiSMAStrategy
import datetime


class TestStrategy(bt.Strategy):
    def next(self):
        pass


def run():
    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)

    assets = ["MSFT", "GOOG", "APPL", "TSLA"]

    for asset in assets:

        data = bt.feeds.YahooFinanceCSVData(
            dataname=f'data/{asset}.csv',
            fromdate=datetime(2021, 1, 1),
            todate=datetime(2021, 12, 31)
        )

        cerebro.adddata(data, name=asset)

    cerebro.addstrategy(MultiSMAStrategy)    

    print("Valor inicial del portfolio:", cerebro.broker.getvalue())

    cerebro.run()

    print("Valor final del portfolio:", cerebro.broker.getvalue())

    cerebro.plot()


if __name__ == "__main__":
    run()
