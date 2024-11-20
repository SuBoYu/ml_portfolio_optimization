import pandas as pd
import talib

label = pd.read_csv("raw_data/100_label.csv")
margin = pd.read_csv("raw_data/100_feature_past_6_months_margin_short.csv")
ohlcv = pd.read_csv("raw_data/100_feature_past_6_months_ohlcv.csv")
industry = pd.read_csv("raw_data/stock_industry.csv")


def calculate_feature(id):
    output = pd.DataFrame()
    for j in range(len(label[label["stock_id"] == id])):
        df = ohlcv[ohlcv["stock_id"] == id].drop(columns=["stock_id", "date"]).iloc[j * 180:(j + 1) * 180]
        date = ohlcv[ohlcv["stock_id"] == id][["date", "stock_id"]].iloc[j * 180:(j + 1) * 180]
        df = df.astype('float')
        for i in talib.get_functions():
            try:
                result = eval('abstract.' + i + f'(ohlcv[ohlcv["stock_id"] == {id}])')

                result.name = i.lower() if type(result) == pd.core.series.Series else None
                df = pd.merge(df, pd.DataFrame(result), left_on=df.index, right_on=result.index)
                df = df.set_index("key_0")
            except:
                print(i)
        df = pd.merge(date, df, left_index=True, right_index=True)  # Specify left_on parameter
        space = pd.merge(df.tail(1), label[label["stock_id"] == id].iloc[j:j + 1], on="stock_id")
        print(j)
        output = pd.concat([output, space])
    return output


def classify_to_binary(profit):
    if profit > 24:
        return 0
    else:
        return 1


def classify(profit):
    if profit > 24:
        return 0
    elif profit >= 13:
        return 1
    elif profit >= 1.08:
        return 2
    else:
        return 3


result = pd.DataFrame()
for id in ohlcv["stock_id"].unique():
    out = calculate_feature(id)
    result = pd.concat([result, out])

result.to_csv("result.csv", index=False)