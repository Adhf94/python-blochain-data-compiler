import requests

from coingeckopy.settings import API_URL

RESOURCE_URL = "/coins"


class CoinsAPI:
    def list(self):
        r = requests.get(f"{API_URL}{RESOURCE_URL}/list/")
        c = r.json()
        print(c)

coinl = CoinsAPI()
coinl.list()