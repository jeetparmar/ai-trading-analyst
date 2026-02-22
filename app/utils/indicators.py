import ta


def add_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["ema20"] = ta.trend.EMAIndicator(df["close"], window=20).ema_indicator()
    df["ema50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    df["macd"] = ta.trend.MACD(df["close"]).macd()
    df["atr"] = ta.volatility.AverageTrueRange(
        df["high"], df["low"], df["close"]
    ).average_true_range()
    return df
