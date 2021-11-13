import yfinance as yf 
import pandas   as pd
import requests
import datetime
import config

#get the average high price for a 3 month period
# def high_prices_average(symbol):
#     data_list           = list()
#     row                 = 0
#     high_prices_sum     = 0
#     high_prices_average = 0

#     #download stock(s) data from yfinance
#     stock = yf.download(
#         tickers     = [symbol],
#         period      = "1wk",
#         progress    = False,
#         auto_adjust = True,
#         actions     = "inline")

#     stock['ticker'] = symbol
#     data_list.append(stock)

#     df = pd.concat(data_list)
#     df = df[["High"]]

#     while row < df.size:
#         high_prices_sum += df.iat[row, 0]
#         row += 1
    
#     #calculate the average price per wanted time
#     high_prices_average = high_prices_sum/ row
    
#     return high_prices_average

def high_prices_average(symbol):
    ALPACA_URL = "https://data.alpaca.markets/v2/stocks/"+symbol+"/bars"

    date_end = datetime.date.today()

    date_start = date_end + datetime.timedelta(weeks = -1)

    data = {'start' : date_start, 'end' : date_end, 'timeframe':'day'}
    request = requests.get(ALPACA_URL, data = data, headers = {"APCA-API-KEY-ID" : config.ACC_KEY, "APCA-API-SECRET-KEY" : config.SECRET_KEY})

    print(request.content)