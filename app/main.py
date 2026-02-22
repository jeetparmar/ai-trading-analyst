from fastapi import FastAPI
from app.config import SYMBOL
from app.agents.market_data_agent import fetch_ohlcv, fetch_fear_greed
from app.agents.technical_agent import generate_technical_signal
from app.agents.sentiment_agent import analyze_sentiment
from app.agents.decision_fusion_agent import fuse_signals
from app.agents.risk_manager_agent import calculate_position_size
from app.execution.paper_executor import PaperTrader

app = FastAPI()
trader = PaperTrader()


@app.get("/analyze")
def analyze():
    df = fetch_ohlcv()
    fear_greed = fetch_fear_greed()

    technical = generate_technical_signal(df)
    sentiment = analyze_sentiment(fear_greed)
    decision = fuse_signals(technical, sentiment)
    
    return {"symbol": SYMBOL, "technical": technical, "sentiment": sentiment, "final_decision": decision}


@app.post("/trade")
def trade():
    df = fetch_ohlcv()
    price = df.iloc[-1]["close"]

    technical = generate_technical_signal(df)
    sentiment = analyze_sentiment(fetch_fear_greed())
    decision = fuse_signals(technical, sentiment)

    size = calculate_position_size(trader.get_balance(), price)
    result = trader.execute_trade(decision, price, size)

    return {
        "symbol": SYMBOL,
        "decision": decision,
        "price": price,
        "size": size,
        "result": result,
        "balance": trader.get_balance(),
    }
