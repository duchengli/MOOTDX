from mootdx import consts
from mootdx.quotes import Quotes
from datetime import datetime, timedelta

client = Quotes.factory(market="std")


def get_stocks():
    stocks = []
    client = Quotes.factory(market="std")
    symbol = client.stocks(market=consts.MARKET_SH)
    for item in symbol["code"].to_list():
        if item[:3] in ["600", "601", "603", "605", "688"]:  # 查询沪市主板和科创板股票代码
            stocks.append(item)

    symbol = client.stocks(market=consts.MARKET_SZ)
    for item in symbol["code"].to_list():
        if item[:3] in ["000", "001", "002", "003", "300", "301"]:
            stocks.append(item)

    return stocks


def get_zongshizhi(stock="000001", delay=0):
    tdate = datetime.now() - timedelta(delay)
    tdate_str = tdate.strftime("%Y/%-m/%-d") + " 15:00"  # windows平台下运行用# linux下用-
    zgb = client.finance(symbol=stock).loc[0, "zongguben"]
    # price = client.bars(symbol=stock, adjust="qfq", frequency=9, offset=1, start=0).loc[
    #     "2023/8/11 15:00", "close"
    # ]
    price = client.bars(symbol=stock, adjust="qfq", frequency=9, offset=1, start=0).loc[
        tdate_str, "close"
    ]
    return round(zgb * price / 100000000, 2)


print(get_zongshizhi("000001", 1))
