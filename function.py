from mootdx import consts
from mootdx.quotes import Quotes

def get_stocks():
    stocks = []
    client = Quotes.factory(market="std")
    symbol = client.stocks(market=consts.MARKET_SH)
    for item in symbol["code"].to_list():
        if item[:3] in ['600','601','603','605','688']:
            stocks.append(item)

    symbol = client.stocks(market=consts.MARKET_SZ)
    for item in symbol["code"].to_list():
        if item[:3] in ['000','001','002','003','300','301']:
            stocks.append(item)
    
    return stocks

my_stocks = get_stocks()
print(2236+2815)
print(len(my_stocks))
