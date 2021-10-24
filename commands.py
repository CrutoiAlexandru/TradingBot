import pandas   as pd 
import yfinance as yf
import sys
import os

def commands_definition():
    global exit_command

    exit_command  = ["quit", "QUIT", "Quit", "Q", "q"]

    print("To exit enter: " + str(exit_command))
    print("To clear data enter: clear")

def clear_command():
    for root, dirs, files in os.walk("csv_stock_data"):
        for file in files:
            os.remove(os.path.join(root, file))

def gather_command(value):
    stock = value#input("Enter the desires stock: ")
    data_list = list()

    data = yf.download(
        tickers = [stock],
        period = "1d",
        progress = False,
        auto_adjust = True,
        actions = "inline")

    data['ticker'] = stock
    data_list.append(data)

    df = pd.concat(data_list)
    df.to_csv('csv_stock_data/'+stock+'.csv')

    print(data.head())
    input_command()

def input_command():
    value = input()

    if value == "clear":
        clear_command()
        input_command()

    if value in exit_command:
        print("Goodbye!")
        sys.exit()
    else:
        gather_command(value)