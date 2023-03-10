import ssl
import time
from config import private_key, relay_manager
from dotenv import load_dotenv
from nostr.event import Event

load_dotenv()

def post_to_relay(message):
  relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})
  time.sleep(5)
  event = Event(public_key=private_key.public_key.hex(), content=message)
  private_key.sign_event(event)
  relay_manager.publish_event(event)
  time.sleep(5)
  relay_manager.close_connections()