from app.config import STARTING_BALANCE


class PaperTrader:
    def __init__(self):
        self.balance = STARTING_BALANCE
        self.positions = []

    def execute_trade(self, decision, price, size):
        if decision in ["BUY", "STRONG_BUY"]:
            cost = price * size
            if cost <= self.balance:
                self.balance -= cost
                self.positions.append({"entry": price, "size": size})
                return "Trade Executed (BUY)"
        return "No Trade"

    def get_balance(self):
        return self.balance
