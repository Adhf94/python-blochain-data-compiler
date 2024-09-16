from typing import List
import requests

from coingeckopy.settings import API_URL

from coingeckopy.apis.coins.schemas import Coin, CoinMarkets


RESOURCE_URL = "/coins"


class CoinsAPI:
    def list(self) -> List[Coin]:
        response = requests.get(f"{API_URL}{RESOURCE_URL}/list/")
        coins = [Coin.parse_obj(coin) for coin in response.json()]
        return coins

    def markets(self, currency="usd", order="market_cap_desc", per_page=100, sparkline="false") -> List[CoinMarkets]:
        response = requests.get(f"{API_URL}{RESOURCE_URL}/markets?vs_currency={currency}")
        coins = [CoinMarkets.parse_obj(coin) for coin in response.json()]
        return coins
