import yfinance as yf 
import pandas   as pd

#get the average low price for a 3 month period
def low_prices_average():
    data_list          = list()
    row                = 0
    low_prices_sum     = 0
    low_prices_average = 0

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
    df = df[["Low"]]

    while row < df.size:
        low_prices_sum  += df.iat[row, 0]
        row += 1
    
    #calculate the average price
    low_prices_average = low_prices_sum / row
    
    print(low_prices_average)