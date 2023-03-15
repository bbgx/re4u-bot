import ssl
import time
from .config import private_key, relay_manager
from dotenv import load_dotenv
from nostr.event import Event

load_dotenv()

def post_to_relay(message):
    with relay_manager_connection() as connection:
        event = create_and_sign_event(message)
        connection.publish_event(event)
        print(message)

def relay_manager_connection():
    class Connection:
        def __enter__(self):
            relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})
            time.sleep(5)
            return relay_manager

        def __exit__(self, exc_type, exc_val, exc_tb):
            time.sleep(5)
            relay_manager.close_connections()

    return Connection()

def create_and_sign_event(message):
    event = Event(public_key=private_key.public_key.hex(), content=message)
    private_key.sign_event(event)
    return event
