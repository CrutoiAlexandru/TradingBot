import time

#find out if the market is open
def market_status():
    if((time.gmtime().tm_hour > 13 and time.gmtime().tm_hour < 20) or (time.gmtime().tm_hour == 13 and time.gmtime().tm_min > 29)):
        return True
    else:
        return False