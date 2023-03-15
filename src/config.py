import os
import pytz
import json
from dotenv import load_dotenv
from cachetools import TTLCache
from nostr.relay_manager import RelayManager
from nostr.key import PrivateKey

load_dotenv()

BASE_URL = os.getenv('BASE_URL', default='https://api.example.com')

TIMEZONE_NAME = "America/Sao_Paulo"
timezone = pytz.timezone(TIMEZONE_NAME)

CACHE_MAXSIZE = 1
CACHE_TTL = 3600
cache = TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL)

NODES_FILENAME = "nodes.json"
with open(NODES_FILENAME, "r") as f:
    nodes = json.load(f)

relay_manager = RelayManager()
for node in nodes:
    relay_manager.add_relay(node["url"])

PRIVATE_KEY_NSEC = os.getenv('NSEC_KEY')
private_key = PrivateKey.from_nsec(PRIVATE_KEY_NSEC)
