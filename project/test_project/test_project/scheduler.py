import time
import datetime
from globals import MARKET_CLOSE_DATES
import os

def isWeekday():
    day = datetime.datetime.today().weekday()
    if day < 6:
        return True
    else:
        return False

def isMarketOpen():
    today_value = datetime.datetime.now().strftime("%b-%d-%y")
    print today_value
    print MARKET_CLOSE_DATES
    if today_value in MARKET_CLOSE_DATES:
        return False
    else:
        return True

print "========== Crawler started ========="
running = False

while True:
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute

    print "current hour = " + str(hour) + " minute = " + str(minute)
    if hour == 23 and minute == 59:
        # reset running to false at midnight. 
        # This does not mean crawling has finished. 
        # This is for avoiding running multiple crawlers for the same day.
        running = False

    if hour == 17 and minute < 5:
        # schdeule a run around 17:00.
        if running == False:            
            if isWeekday():
                print "[Weekday]"
                if isMarketOpen():
                    print "[Market is OPEN]"
                    pid = os.fork()
                    if pid == 0:
                        execfile('work.py')
                        exit()
                    else:
                        running = True
                else:
                    print "[Market CLOSED]"
            else:
                print "[Weekend]"

    time.sleep(60)