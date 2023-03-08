import requests
from config import BASE_URL, private_key, relay_manager
from nostr.event import Event

def get_current_rate():
    try:
        response = requests.get(BASE_URL)
        data = response.json()
        return float(data["USDBRL"]["bid"])
    except:
        return None

def compare_rates(previous_rate, current_rate):
    if previous_rate is None:
        previous_rate = current_rate
    else:
        if round(current_rate, 2) > round(previous_rate, 2):
            event = Event(public_key=private_key.public_key.hex(), content=f"O dólar subiu! O dólar está R$ {current_rate:.2f}.")
            private_key.sign_event(event)
            relay_manager.publish_event(event)
            print('Posted')
        elif round(current_rate, 2) < round(previous_rate, 2):
            event = Event(public_key=private_key.public_key.hex(), content=f"O dólar caiu! O dólar está R$ {current_rate:.2f}.")
            private_key.sign_event(event)
            relay_manager.publish_event(event)
            print('Posted')
        elif round(current_rate, 2) == round(previous_rate, 2):
            event = Event(public_key=private_key.public_key.hex(), content=f"O dólar continua R$ {current_rate:.2f}. Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. Vai todo mundo perder..")
            private_key.sign_event(event)
            relay_manager.publish_event(event)
            print('Posted')
    return current_rate
