import requests
from config import BASE_URL
from post_to_relay import post_to_relay

def get_current_rate():
  try:
    response = requests.get(BASE_URL)
    data = response.json()
    return float(data["USDBRL"]["bid"])
  except:
    return None

def compare_rates(previous_rate, current_rate):
  previous_rate = current_rate
  if round(current_rate, 2) > round(previous_rate, 2):
    post_to_relay(f"O dólar subiu! O dólar está R$ {current_rate:.2f}.")
  elif round(current_rate, 2) < round(previous_rate, 2):
    post_to_relay(f"O dólar caiu! O dólar está R$ {current_rate:.2f}.")
  elif round(current_rate, 2) == round(previous_rate, 2):
    post_to_relay(f"O dólar continua R$ {current_rate:.2f}. Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. Vai todo mundo perder..")
  return current_rate
