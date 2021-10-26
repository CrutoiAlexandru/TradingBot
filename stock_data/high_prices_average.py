import yfinance as yf 
import pandas   as pd



def high_prices_average():
    data_list           = list()
    row                 = 0
    high_prices_sum     = 0
    high_prices_average = 0

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
    
    high_prices_average = high_prices_sum/ row
    
    print(high_prices_average)

    #df.to_csv('csv_stock_data/'+'tsla'+'.csv')

    #print(df)    