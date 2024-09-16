import responses

from coingeckopy.apis.coins.schemas import Coin, CoinMarkets
from coingeckopy.settings import API_URL
from coingeckopy.apis.coins.CoinsAPI import RESOURCE_URL, CoinsAPI


@responses.activate
def test_list_success():
    # GIVEN
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

    coins_api = CoinsAPI()
    # WHEN
    coins = coins_api.list()

    # THEN
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == f"{API_URL}{RESOURCE_URL}/list/"

    for index, coin in enumerate(coins):
        assert isinstance(coin, Coin)
        assert coin.id == list_endpoint_response[index]["id"]
        assert coin.symbol == list_endpoint_response[index]["symbol"]
        assert coin.name == list_endpoint_response[index]["name"]


@responses.activate
def test_markets_success():
    # GIVEN
    market_endpoint_response = [
        {
            "id": 'bitcoin',
            "symbol": 'btc',
            "name": 'Bitcoin',
            "image": 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579',
            "current_price": '40328',
            "market_cap": '770872874169',
            "market_cap_rank": '1',
            "fully_diluted_valuation": '852687779347',
            "total_volume": '30620850477',
            "high_24h": '41551',
            "low_24h": '39029',
            "price_change_24h": '1177.83',
            "price_change_percentage_24h": '3.00844',
            "market_cap_change_24h": '28163613878',
            "market_cap_change_percentage_24h": '3.79201',
            "circulating_supply": '18985062.0',
            "total_supply": '21000000.0',
            "max_supply": '21000000.0',
            "ath": '69045',
            "ath_change_percentage": '-41.6621',
            "ath_date": '2021-11-10T14:24:11.849Z',
            "atl": '67.81',
            "atl_change_percentage": '59301.06712',
            "atl_date": '2013-07-06T00:00:00.000Z',
            "last_updated": '2022-03-16T17:28:52.369Z'
        },
        {
            "id": "ethereum",
            "symbol": "eth",
            "name": "Ethereum",
            "image": "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880",
            "current_price": "2870.88",
            "market_cap": "344397373070",
            "market_cap_rank": "2",
            "fully_diluted_valuation": None,
            "total_volume": "11344144317",
            "high_24h": "2962.25",
            "low_24h": "2826.26",
            "price_change_24h": "-80.188600541185",
            "price_change_percentage_24h": "-2.71727",
            "market_cap_change_24h": "-9974098897.733337",
            "market_cap_change_percentage_24h": "-2.81459",
            "circulating_supply": "120041484.499",
            "total_supply": None,
            "max_supply": None,
            "ath": "4878.26",
            "ath_change_percentage": "-41.25878",
            "ath_date": "2021-11-10T14:24:19.604Z",
            "atl": "0.432979",
            "atl_change_percentage": "661722.05579",
            "atl_date": "2015-10-20T00:00:00.000Z",
            "roi": {
                "times": "91.84498150455758",
                "currency": "btc",
                "percentage": "9184.498150455758"
            },
            "last_updated": "2022-03-20T19:52:54.867Z"
        },
    ]
    responses.add(responses.GET,
                  f"{API_URL}{RESOURCE_URL}/markets?vs_currency=usd",
                  json=market_endpoint_response, status=200)

    coins_api = CoinsAPI()
    # WHEN
    markets = coins_api.markets()

    # THEN
    assert len(responses.calls) == 1
    assert responses.calls[
               0].request.url == f"{API_URL}{RESOURCE_URL}/markets?vs_currency=usd"

    for index, market in enumerate(markets):
        assert isinstance(market, CoinMarkets)
        assert market.id == market_endpoint_response[index]["id"]
        assert market.symbol == market_endpoint_response[index]["symbol"]
        assert market.name == market_endpoint_response[index]["name"]
        assert market.image == market_endpoint_response[index]["image"]
        assert market.current_price == market_endpoint_response[index]["current_price"]
        assert market.market_cap == market_endpoint_response[index]["market_cap"]
        assert market.market_cap_rank == market_endpoint_response[index]["market_cap_rank"]
        assert market.fully_diluted_valuation == market_endpoint_response[index]["fully_diluted_valuation"]
        assert market.total_volume == market_endpoint_response[index]["total_volume"]
        assert market.high_24h == market_endpoint_response[index]["high_24h"]
        assert market.low_24h == market_endpoint_response[index]["low_24h"]
        assert market.price_change_24h == market_endpoint_response[index]["price_change_24h"]
        assert market.price_change_percentage_24h == market_endpoint_response[index]["price_change_percentage_24h"]
        assert market.market_cap_change_24h == market_endpoint_response[index]["market_cap_change_24h"]
        assert market.market_cap_change_percentage_24h == market_endpoint_response[index][
            "market_cap_change_percentage_24h"]
        assert market.circulating_supply == market_endpoint_response[index]["circulating_supply"]
        assert market.max_supply == market_endpoint_response[index]["max_supply"]
        assert market.ath == market_endpoint_response[index]["ath"]
        assert market.ath_change_percentage == market_endpoint_response[index]["ath_change_percentage"]
        assert market.ath_date == market_endpoint_response[index]["ath_date"]
        assert market.atl == market_endpoint_response[index]["atl"]
        assert market.atl_change_percentage == market_endpoint_response[index]["atl_change_percentage"]
        assert market.atl_date == market_endpoint_response[index]["atl_date"]
        assert market.last_updated == market_endpoint_response[index]["last_updated"]
