import yfinance as yf 
import pandas   as pd

def low_prices_average():
    data_list          = list()
    row                = 0
    low_prices_sum     = 0
    low_prices_average = 0

    stock = yf.download(
        tickers     = ['tsla'],
        period      = "3mo",
        progress    = False,
        auto_adjust = True,
        actions     = "inline")

    stock['ticker'] = 'tsla'
    data_list.append(stock)

    df = pd.concat(data_list)
    df = df[["Low"]]

    while row < df.size:
        low_prices_sum  += df.iat[row, 0]
        row += 1
    
    low_prices_average = low_prices_sum / row
    
    print(low_prices_average)