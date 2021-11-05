import yfin.high_prices_average as ha
import yfin.low_prices_average  as la

def good_to_buy(price, symbol):
    #print(ha.high_prices_average(symbol))
    print(la.low_prices_average(symbol))
    return False

def good_to_sell(price, symbol):
    return False    