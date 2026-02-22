import ccxt
import pandas as pd
import requests
from app.config import SYMBOL, TIMEFRAME, CANDLE_LIMIT

exchange = ccxt.binance()


def fetch_ohlcv():
    ohlcv = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit=CANDLE_LIMIT)
    df = pd.DataFrame(
        ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df


def fetch_fear_greed():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()
    return int(data["data"][0]["value"])
