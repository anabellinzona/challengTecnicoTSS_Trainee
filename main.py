import backtrader as bt
from strategies.multiSMAStrategy import MultiSMAStrategy


class TestStrategy(bt.Strategy):
    def next(self):
        pass


def run():
    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)

    cerebro.addstrategy(MultiSMAStrategy)

    data = bt.feeds.GenericCSVData(
        dataname='data/msft.csv',
        dtformat='%Y-%m-%d',
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1,
        headers=True
    )


    cerebro.adddata(data)

    print("Valor inicial del portfolio:", cerebro.broker.getvalue())

    cerebro.run()

    print("Valor final del portfolio:", cerebro.broker.getvalue())

    cerebro.plot()


if __name__ == "__main__":
    run()
