from abc import ABC, abstractmethod
from typing import List, Dict
import random
import time


class StockMarket:
    """Represents a stock market"""

    def __init__(self):
        self._observers: List[StockObserver] = []
        self._stocks: Dict[str, float] = {
            "AAPL": 150.0,
            "GOOGL": 2800.0,
            "MSFT": 300.0,
            "AMZN": 3300.0,
            "FB": 330.0
        }

    def attach(self, observer: 'StockObserver'):
        """Attach an observer to the stock market."""
        self._observers.append(observer)

    def detach(self, observer: 'StockObserver'):
        """Detach an observer from the stock market."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers of stock price changes."""
        for observer in self._observers:
            observer.update(self._stocks)

    def update_prices(self):
        """Simulate stock price changes."""
        for stock in self._stocks:
            change = random.uniform(-0.05, 0.05)  # Random change between -5% and 5%
            self._stocks[stock] *= (1 + change)
        self.notify()


class StockObserver(ABC):
    """Abstract base class for stock observers."""

    @abstractmethod
    def update(self, stocks: Dict[str, float]):
        """Update method called when stock prices change."""
        pass


class StockAnalyst(StockObserver):
    """Represents a stock analyst observing the market."""

    def __init__(self, name: str):
        self.name = name

    def update(self, stocks: Dict[str, float]):
        print(f"\n{self.name} - Market Analysis:")
        for stock, price in stocks.items():
            print(f"  {stock}: ${price:.2f}")
        print(f"  Overall market trend: {self._analyze_trend(stocks)}")

    def _analyze_trend(self, stocks: Dict[str, float]) -> str:
        """Simple trend analysis based on average price movement."""
        prev_prices = {stock: price * random.uniform(0.98, 1.02) for stock, price in stocks.items()}
        changes = [stocks[stock] - prev_prices[stock] for stock in stocks]
        avg_change = sum(changes) / len(changes)
        if avg_change > 0:
            return "Bullish 📈"
        elif avg_change < 0:
            return "Bearish 📉"
        else:
            return "Neutral ↔️"


class InvestmentBot(StockObserver):
    """Represents an automated investment bot."""

    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.portfolio: Dict[str, float] = {}

    def update(self, stocks: Dict[str, float]):
        print(f"\n{self.name} - Investment Bot:")
        self._make_investment_decision(stocks)
        self._display_portfolio()

    def _make_investment_decision(self, stocks: Dict[str, float]):
        """Simple investment strategy: invest in the cheapest stock."""
        if self.budget > 0:
            cheapest_stock = min(stocks, key=stocks.get)
            investment_amount = min(self.budget, stocks[cheapest_stock])
            shares = investment_amount / stocks[cheapest_stock]

            if cheapest_stock in self.portfolio:
                self.portfolio[cheapest_stock] += shares
            else:
                self.portfolio[cheapest_stock] = shares

            self.budget -= investment_amount
            print(f"  Invested ${investment_amount:.2f} in {cheapest_stock}")
        else:
            print("  No budget left for investments")

    def _display_portfolio(self):
        print("  Current Portfolio:")
        for stock, shares in self.portfolio.items():
            print(f"    {stock}: {shares:.2f} shares")
        print(f"  Remaining Budget: ${self.budget:.2f}")


class StockAlert(StockObserver):
    """Represents a stock price alert system."""

    def __init__(self, threshold: float):
        self.threshold = threshold
        self.previous_prices: Dict[str, float] = {}

    def update(self, stocks: Dict[str, float]):
        print("\nStock Price Alerts:")
        for stock, price in stocks.items():
            if stock in self.previous_prices:
                change = (price - self.previous_prices[stock]) / self.previous_prices[stock]
                if abs(change) >= self.threshold:
                    direction = "up ⬆️" if change > 0 else "down ⬇️"
                    print(f"  ❗ {stock} moved {direction} by {abs(change) * 100:.2f}%")
            self.previous_prices[stock] = price


def run_stock_market_simulation(days: int):
    """Run a stock market simulation for a specified number of days."""
    market = StockMarket()

    # Create and attach observers
    analyst = StockAnalyst("John Doe")
    bot = InvestmentBot("TradingBot3000", 10000)
    alert = StockAlert(0.03)  # 3% threshold

    market.attach(analyst)
    market.attach(bot)
    market.attach(alert)

    print("Starting stock market simulation...")
    for day in range(1, days + 1):
        print(f"\nDay {day}:")
        market.update_prices()
        time.sleep(1)  # Pause for readability


if __name__ == "__main__":
    run_stock_market_simulation(5)  # Simulate for 5 days
