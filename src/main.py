import time
from config import timezone, cache
from utils import get_current_rate, compare_rates
from datetime import datetime

while True:
    current_time = datetime.now(timezone)

    if current_time.hour >= 10 and current_time.hour < 18:
        current_rate = get_current_rate()

        if current_time.hour == 10 and current_time.minute == 0:
            previous_rate = cache.get('previous_rate')
        else:
            previous_rate = compare_rates(cache.get('previous_rate'), current_rate)
            cache['previous_rate'] = previous_rate


    time.sleep(3600)
