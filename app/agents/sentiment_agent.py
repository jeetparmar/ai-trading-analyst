def analyze_sentiment(fear_greed_value):
    if fear_greed_value < 30:
        return {"sentiment": "BEARISH"}
    elif fear_greed_value > 60:
        return {"sentiment": "BULLISH"}
    else:
        return {"sentiment": "NEUTRAL"}
