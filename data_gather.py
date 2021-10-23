import pandas   as pd 
import yfinance as yf

def exit():
    global exit_command
    exit_command = ["quit", "QUIT", "Quit", "Q", "q"]
    print("To exit enter: " + str(exit_command))

def gather():
    stock = input("Enter the desires stock: ")

    if stock in exit_command:
        print("Goodbye!")
        return 0
    
    data = yf.download(
        tickers = [stock],
        period = "1d",
        progress = False,
        auto_adjust = True,
        actions = "inline")

    print(data.head())
    gather()

    

