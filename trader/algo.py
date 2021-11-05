import yfin.high_prices_average as ha
import yfin.low_prices_average  as la

#be advised that:
#the algorithms are very primitive and do not implement safety mesures
#in the case our symbol drop too much in value
#they are not chosen with care because they are strictly for paper-trading
#at the moment I do not have experience in stock trading

#simple algo for buying stock
def good_to_buy(price, symbol):
    #if the current price of our symbol is lower than the weekly(as chosen by us)
    #low average of the symbol it means we are good to buy
    #we are buying bellow the average so when it grows we sell
    if price < la.low_prices_average(symbol):
        return True
    else:
        return False

#simple algo for selling stock
def good_to_sell(price, symbol):
    #if the current price of our symbol is higher than the weekly(as chosen by us)
    #high average of the symbol it means we are good to sell
    #we are selling above the average so we get a profit
    if price > ha.high_prices_average(symbol):
        return True
    else:
        return False    