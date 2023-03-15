import time
import schedule
from config import timezone, cache
from utils import get_current_rate, compare_rates
from datetime import datetime, timedelta

def reset_cache():
    current_time = datetime.now(timezone)
    if current_time.hour == 0 and current_time.minute == 0:
        cache.clear()

def get_and_compare_rate():
    current_time = datetime.now(timezone)
    if is_weekday(current_time) and is_business_hours(current_time):
        current_rate = get_current_rate()

        if not is_hour_beginning(current_time):
            compare_rates(cache.get('previous_rate'), current_rate)
        
        cache['previous_rate'] = current_rate

def is_weekday(current_time):
    return current_time.weekday() < 5

def is_business_hours(current_time):
    return 10 <= current_time.hour < 23

def is_hour_beginning(current_time):
    return current_time.hour == 10 and current_time.minute == 0

schedule.every().minute.do(get_and_compare_rate)
schedule.every().day.at("00:00").do(reset_cache)

while True:
    schedule.run_pending()
    time.sleep(1)
