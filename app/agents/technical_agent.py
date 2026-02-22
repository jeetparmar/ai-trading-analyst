from app.utils.indicators import add_indicators


def generate_technical_signal(df):
    df = add_indicators(df)
    latest = df.iloc[-1]

    signal = "HOLD"
    confidence = 0.5

    if latest["rsi"] < 30 and latest["ema20"] > latest["ema50"]:
        signal = "BUY"
        confidence = 0.75
    elif latest["rsi"] > 70 and latest["ema20"] < latest["ema50"]:
        signal = "SELL"
        confidence = 0.75

    return {"signal": signal, "confidence": confidence, "volatility": latest["atr"]}
