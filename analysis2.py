from mootdx import consts
from mootdx.quotes import Quotes

stocks = []
client = Quotes.factory(market="std")
symbol = client.stocks(market=consts.MARKET_SH)
for item in symbol["code"].to_list():
    if item[:3] in ["600", "601", "603", "688"]:
        # print(item)
        stocks.append(item)

symbol = client.stocks(market=consts.MARKET_SZ)
for item in symbol["code"].to_list():
    if item[:3] in ["000", "300", "002"]:
        # print(item)
        stocks.append(item)
print(len(stocks))

# symbol['name'].to_list()
# symbol[symbol['name']=='中国国航']
# symbol["type"] = symbol["code"].apply(lambda x: x[:3])
# print(symbol.head(20))
# print(symbol.groupby("type").agg("count").sort_values(by='code', ascending=False))


# client = Quotes.factory(market="std")
# client.finance(symbol="600300")
# print(client.finance(symbol="600300").columns)
