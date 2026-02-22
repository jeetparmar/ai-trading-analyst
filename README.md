# AI Trading Analyst

A FastAPI service that analyzes market conditions for `BTC/USDT` and simulates paper trades using:

- market data from Binance via `ccxt`
- technical indicators (RSI, EMA, ATR)
- sentiment from the Fear & Greed Index
- simple multi-agent decision fusion and risk sizing

## Project Structure

```text
app/
  main.py                      # FastAPI app and API routes
  config.py                    # Trading and risk configuration
  agents/
    market_data_agent.py       # OHLCV + Fear & Greed fetchers
    technical_agent.py         # Technical signal generation
    sentiment_agent.py         # Sentiment classification
    decision_fusion_agent.py   # Signal fusion logic
    risk_manager_agent.py      # Position sizing + daily loss checks
  execution/
    paper_executor.py          # In-memory paper trading executor
  utils/
    indicators.py              # Indicator calculations
```

## Requirements

- Python 3.10+
- Internet access for Binance/Fear & Greed APIs

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

From the repository root:

```bash
uvicorn app.main:app --reload
```

Server default URL: `http://127.0.0.1:8000`

## API Endpoints

### `GET /analyze`

Fetches current data and returns:

- symbol
- technical signal + confidence + volatility
- sentiment classification
- fused final decision

Example:

```bash
curl http://127.0.0.1:8000/analyze
```

### `POST /trade`

Runs analysis, calculates position size from current balance and risk settings, and executes a paper trade if criteria are met.

Returns:

- symbol
- decision
- current price
- calculated size
- execution result
- updated balance

Example:

```bash
curl -X POST http://127.0.0.1:8000/trade
```

## Configuration

Tune behavior in `app/config.py`:

- `SYMBOL` (default `BTC/USDT`)
- `TIMEFRAME` (default `1h`)
- `CANDLE_LIMIT` (default `200`)
- `MAX_RISK_PER_TRADE` (default `0.01`)
- `MAX_DAILY_LOSS` (default `0.03`)
- `STARTING_BALANCE` (default `10000`)

## Notes

- Paper trading state is in-memory; balance and positions reset when the app restarts.
- This project is for research/education and not financial advice.
