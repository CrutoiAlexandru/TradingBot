import yfinance as yf

def current_price():
    stock = yf.Ticker("TSLA")
    price = stock.info['regularMarketPrice']
    print(price)