import pytest
import responses

from coingeckopy.apis.coins.schemas import Coin
from coingeckopy.settings import API_URL
from coingeckopy.apis.coins.CoinsAPI import RESOURCE_URL, CoinsAPI

@responses.activate
def test_list_success():
    #GIVEN
    list_endpoint_response = [
        {
            "id": "01coin",
            "symbol": "zoc",
            "name": "01coin"
        },
        {
            "id": "0-5x-long-algorand-token",
            "symbol": "algohalf",
            "name": "0.5X Long Algorand Token"
        }]

    responses.add(responses.GET, f"{API_URL}{RESOURCE_URL}/list/",
                  json=list_endpoint_response, status=200)

    list_when_response = CoinsAPI()
    #WHEN
    coins = list_when_response.list()

    #THEN
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == f"{API_URL}{RESOURCE_URL}/list/"

    for index, coin in enumerate(coins):
        assert isinstance(coin, Coin)
        assert coin.id == list_endpoint_response[index]["id"]
        assert coin.symbol == list_endpoint_response[index]["symbol"]
        assert coin.name == list_endpoint_response[index]["name"]

def test_list_error()