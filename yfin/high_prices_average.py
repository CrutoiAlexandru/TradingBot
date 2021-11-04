import yfinance as yf 
import pandas   as pd

#get the average high price for a 3 month period
def high_prices_average():
    data_list           = list()
    row                 = 0
    high_prices_sum     = 0
    high_prices_average = 0

    #download stock(s) data from yfinance
    stock = yf.download(
        tickers     = ['tsla'],
        period      = "3mo",
        progress    = False,
        auto_adjust = True,
        actions     = "inline")

    stock['ticker'] = 'tsla'
    data_list.append(stock)

    df = pd.concat(data_list)
    df = df[["High"]]

    while row < df.size:
        high_prices_sum += df.iat[row, 0]
        row += 1
    
    #calculate the average price
    high_prices_average = high_prices_sum/ row
    
    print(high_prices_average)