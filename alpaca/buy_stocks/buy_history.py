import json

#create a json file that will remember the buying price of a stock
def buy_history_json(symbol, price):
    data = json.dumps({symbol:price})

    with open("trading_data/" + symbol + ".json", "w") as jsonFile:
        json.dump(data, jsonFile)