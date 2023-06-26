import pandas as pd
from matplotlib import pyplot
from mootdx.contrib.adjust import get_adjust_year
from statsmodels.tsa.seasonal import seasonal_decompose

df2013 = get_adjust_year(symbol="000001", year="2013", factor="01")
df2014 = get_adjust_year(symbol="000001", year="2014", factor="01")
df2015 = get_adjust_year(symbol="000001", year="2015", factor="01")
df2016 = get_adjust_year(symbol="000001", year="2016", factor="01")
df2017 = get_adjust_year(symbol="000001", year="2017", factor="01")
df2018 = get_adjust_year(symbol="000001", year="2018", factor="01")
df2019 = get_adjust_year(symbol="000001", year="2019", factor="01")
df2020 = get_adjust_year(symbol="000001", year="2020", factor="01")
df2021 = get_adjust_year(symbol="000001", year="2021", factor="01")
df2022 = get_adjust_year(symbol="000001", year="2022", factor="01")
df2023 = get_adjust_year(symbol="000001", year="2023", factor="01")

df = pd.concat(
    [
        df2013,
        df2014,
        df2015,
        df2016,
        df2017,
        df2018,
        df2019,
        df2020,
        df2021,
        df2022,
        df2023,
    ],
    # ignore_index=True
)
print(df.info())


# result = seasonal_decompose(df["close"], model="additive")
# # result.plot()
# # pyplot.show()
# print(result.trend)
# print(result.seasonal)
# print(result.resid)
# print(result.observed)
