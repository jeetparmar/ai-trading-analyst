def fuse_signals(technical, sentiment):
    if technical["signal"] == "BUY" and sentiment["sentiment"] == "BULLISH":
        return "STRONG_BUY"
    if technical["signal"] == "SELL" and sentiment["sentiment"] == "BEARISH":
        return "STRONG_SELL"
    return technical["signal"]
