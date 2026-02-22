from app.config import MAX_RISK_PER_TRADE, MAX_DAILY_LOSS


def calculate_position_size(balance, price):
    risk_amount = balance * MAX_RISK_PER_TRADE
    return risk_amount / price


def check_daily_loss(daily_pnl, balance):
    if daily_pnl < -(balance * MAX_DAILY_LOSS):
        return False
    return True
