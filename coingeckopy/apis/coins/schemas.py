from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Coin(BaseModel):
    id: str
    symbol: str
    name: str


class CoinMarkets(BaseModel):

    id: str
    symbol: str
    name: str
    image: str
    current_price: str
    market_cap: str
    market_cap_rank: str
    fully_diluted_valuation: Optional[str] = None
    total_volume: str
    high_24h: str
    low_24h: str
    price_change_24h: str
    price_change_percentage_24h: str
    market_cap_change_24h: str
    market_cap_change_percentage_24h: str
    circulating_supply: str
    total_supply: Optional[str] = None
    max_supply: Optional[str]
    ath: str
    ath_change_percentage: str
    ath_date: str
    atl: str
    atl_change_percentage: str
    atl_date: str
    last_updated: str
