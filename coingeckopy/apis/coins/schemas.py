from pydantic import BaseModel


class Coin(BaseModel):
    id: str
    symbol: str
    name: str

