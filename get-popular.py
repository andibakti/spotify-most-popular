import requests
from pprint import pprint
from datetime import date
from datetime import timedelta
import time
import json
import wget
import utils

#https://spotifycharts.com/viral/global/weekly/2017-12-28--2017-12-28/download
base_url = "https://spotifycharts.com/regional/global/weekly/"

def getpopular():
    # .isoformat()
    day = date(2018, 1, 5)
    # https://spotifycharts.com/regional/global/weekly/2018-01-05--2018-01-12/download
    while(day <= date.today()):
        second_day = day + timedelta(days=7)
        page_url = base_url + str(day.isoformat()) + '--' + str(second_day.isoformat()) + '/download'
        day = second_day
        try:
            response = requests.get(page_url)
            with open('data/' + str(day.isoformat()) + '.csv', 'w+') as f:
                f.write(str(response.content))
                f.close()
            time.sleep(0.02)
        except:
            print('Could not get data')

def getviral():
    base_url = "https://spotifycharts.com/viral/global/daily/"
    # .isoformat()
    day = date(2018, 1, 1)
    while(day <= date.today()):
        second_day = day + timedelta(days=1)
        page_url = base_url + str(day.isoformat()) + '/download'
        try:
            response = requests.get(page_url)
            with open('viral/data/' + str(day.isoformat()) + '.csv', 'w+') as f:
                f.write(str(response.content))
                f.close()
        except:
            print('Could not get data')

        utils.currentDay(day)
        day = second_day
        time.sleep(0.02)

getviral()
