import yfinance as yf

#get current stock price
def current_price():
    stock = yf.Ticker("TSLA")
    price = stock.info['regularMarketPrice']
    print(price)