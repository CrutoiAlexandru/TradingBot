import pandas as pd 

import yfinance as yf

def gather():
    data = yf.download(["TSLA", "GOOGL"],
    start = '2020-09-15', 
    end = '2020-11-15',
    progress = False)

    print(data.head())
