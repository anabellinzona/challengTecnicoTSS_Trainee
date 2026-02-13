import backtrader as bt
from strategies.multiSMAStrategy import MultiSMAStrategy
from datetime import datetime


class TestStrategy(bt.Strategy):
    def next(self):
        pass


def run():
    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)

    assets = ["MSFT", "GOOG", "AAPL", "TSLA"]

    for asset in assets:

       data = bt.feeds.GenericCSVData(
            dataname=f"data/{asset}.csv",

            fromdate=datetime(2021, 1, 1),
            todate=datetime(2021, 12, 31),

            dtformat="%Y-%m-%d",

            datetime=0,
            open=4,
            high=2,
            low=3,
            close=1,
            volume=5,
            openinterest=-1
        )
       
       cerebro.adddata(data, name=asset)

    cerebro.addstrategy(MultiSMAStrategy)    

    print("Valor inicial del portfolio:", cerebro.broker.getvalue())

    cerebro.run(runonce=False)

    print("Valor final del portfolio:", cerebro.broker.getvalue())

    cerebro.plot()


if __name__ == "__main__":
    run()
