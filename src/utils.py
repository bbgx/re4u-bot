import requests
from config import BASE_URL
from post_to_relay import post_to_relay

def get_current_rate():
  try:
    response = requests.get(BASE_URL)
    response.raise_for_status() # Raises an exception for a 4xx or 5xx status code
    data = response.json()
    return float(data["USDBRL"]["bid"])
  except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the exchange rate: {e}")
    return None

def compare_rates(previous_rate, current_rate):
  updated_rate = current_rate
  if round(current_rate, 2) > round(previous_rate, 2):
    post_to_relay(f"O dólar subiu! O dólar está R$ {current_rate:.2f}.")
  elif round(current_rate, 2) < round(previous_rate, 2):
    post_to_relay(f"O dólar caiu! O dólar está R$ {current_rate:.2f}.")
  elif round(current_rate, 2) == round(previous_rate, 2):
    post_to_relay(f"O dólar continua R$ {current_rate:.2f}. Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. Vai todo mundo perder..")
  return updated_rate
