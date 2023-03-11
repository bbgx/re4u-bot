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
    if current_time.hour >= 10 and current_time.hour < 18:
        current_rate = get_current_rate()

        if current_time.hour != 10 or current_time.minute != 0:
            compare_rates(cache.get('previous_rate'), current_rate)
        
        cache['previous_rate'] = current_rate

schedule.every().hour.at(":00").do(get_and_compare_rate)
schedule.every().day.at("00:00").do(reset_cache)

while True:
    schedule.run_pending()
    time.sleep(1)
