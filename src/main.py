import time
from config import timezone, cache
from utils import get_current_rate, compare_rates
from datetime import datetime
import schedule


def get_and_compare_rate():
    current_time = datetime.now(timezone)
    print(current_time)
    if current_time.hour >= 1 and current_time.hour < 23:
        print('The bot is operating!')
        current_rate = get_current_rate()

        if current_time.hour == 10 and current_time.minute == 0:
            print('It is 10am!')
            previous_rate = cache.get('previous_rate')
        else:
            print('Posting the exchange rate!')
            previous_rate = compare_rates(cache.get('previous_rate'), current_rate)
            cache['previous_rate'] = previous_rate

schedule.every().hour.at(":00").do(get_and_compare_rate)

while True:
    schedule.run_pending()
    time.sleep(1)
