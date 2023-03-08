import os
import pytz
import ssl
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta
from cachetools import TTLCache
from nostr.relay_manager import RelayManager
from nostr.key import PrivateKey

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

timezone = pytz.timezone("America/Sao_Paulo")

cache = TTLCache(maxsize=1, ttl=3600)

with open("nodes.json", "r") as f:
    nodes = json.load(f)

relay_manager = RelayManager()
relay_manager = RelayManager()
for node in nodes:
    relay_manager.add_relay(node["url"])
relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification
private_key = PrivateKey.from_nsec(os.getenv('NSEC_KEY'))
