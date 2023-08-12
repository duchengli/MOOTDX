import function as FN
import time

stocks_list = FN.get_stocks()
# print(stocks_list)
# print(FN.get_zongshizhi("600300", 1))
for stock in stocks_list:
    time.sleep(2)
    print(stock + ": " + str(FN.get_zongshizhi(stock, 1)))
