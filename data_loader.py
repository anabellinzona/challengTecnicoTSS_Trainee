import backtrader as bt

def load_data(path):
    return bt.feeds.GenericCSVData(
        dataname=path,
        dtformat='%Y-%m-%d',
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1
    )
