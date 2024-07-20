from abc import ABC, abstractmethod
from typing import List, Dict
import random


class StockExchange:
    """Simulates a stock exchange."""

    def __init__(self):
        self.stocks = {
            "AAPL": 150.0,
            "GOOGL": 2800.0,
            "MSFT": 300.0,
            "AMZN": 3300.0,
            "FB": 330.0
        }

    def get_price(self, symbol: str) -> float:
        return self.stocks.get(symbol, 0.0)

    def execute_trade(self, symbol: str, quantity: int, is_buy: bool) -> bool:
        if symbol not in self.stocks:
            return False
        if is_buy:
            print(f"Bought {quantity} shares of {symbol}")
        else:
            print(f"Sold {quantity} shares of {symbol}")
        return True


class RiskAnalyzer:
    """Analyzes risk for a given trade."""

    def analyze_risk(self, symbol: str, quantity: int) -> str:
        risk_factor = random.uniform(0, 1)
        if risk_factor < 0.3:
            return "Low"
        elif risk_factor < 0.7:
            return "Medium"
        else:
            return "High"


class TaxCalculator:
    """Calculates taxes for a given trade."""

    def calculate_tax(self, profit: float) -> float:
        return profit * 0.2  # Assume 20% tax rate


class TradeLogger:
    """Logs trade details."""

    def log_trade(self, symbol: str, quantity: int, price: float, is_buy: bool):
        action = "Bought" if is_buy else "Sold"
        print(f"LOGGED: {action} {quantity} shares of {symbol} at ${price:.2f}")


class TradingBot(ABC):
    """Abstract base class for trading bots."""

    @abstractmethod
    def should_buy(self, symbol: str, price: float) -> bool:
        pass

    @abstractmethod
    def should_sell(self, symbol: str, price: float) -> bool:
        pass


class SimpleTradingBot(TradingBot):
    """A simple trading bot implementation."""

    def should_buy(self, symbol: str, price: float) -> bool:
        # Simple strategy: buy if price is below 200
        return price < 200

    def should_sell(self, symbol: str, price: float) -> bool:
        # Simple strategy: sell if price is above 1000
        return price > 1000


class TradingFacade:
    """Facade for the trading system, simplifying complex trading operations."""

    def __init__(self):
        self.exchange = StockExchange()
        self.risk_analyzer = RiskAnalyzer()
        self.tax_calculator = TaxCalculator()
        self.logger = TradeLogger()
        self.trading_bot = SimpleTradingBot()

    def analyze_and_trade(self, symbol: str, quantity: int):
        price = self.exchange.get_price(symbol)
        if price == 0.0:
            print(f"Error: Stock {symbol} not found")
            return

        # Analyze risk
        risk_level = self.risk_analyzer.analyze_risk(symbol, quantity)
        print(f"Risk level for this trade: {risk_level}")

        # Decide whether to buy or sell
        if self.trading_bot.should_buy(symbol, price):
            action = "buy"
        elif self.trading_bot.should_sell(symbol, price):
            action = "sell"
        else:
            print("No action recommended by the trading bot")
            return

        # Execute trade
        success = self.exchange.execute_trade(symbol, quantity, action == "buy")
        if success:
            self.logger.log_trade(symbol, quantity, price, action == "buy")

            # Calculate and report taxes (assuming a profit for simplicity)
            profit = quantity * price * 0.1  # Assume 10% profit
            tax = self.tax_calculator.calculate_tax(profit)
            print(f"Estimated tax on profit: ${tax:.2f}")
        else:
            print("Trade execution failed")


def run_trading_simulation():
    """Simulate trading operations using the TradingFacade."""
    facade = TradingFacade()

    print("Scenario 1: Analyzing and trading AAPL")
    facade.analyze_and_trade("AAPL", 10)

    print("\nScenario 2: Analyzing and trading GOOGL")
    facade.analyze_and_trade("GOOGL", 5)

    print("\nScenario 3: Analyzing and trading MSFT")
    facade.analyze_and_trade("MSFT", 15)

    print("\nScenario 4: Attempting to trade an non-existent stock")
    facade.analyze_and_trade("INVALID", 100)


class PortfolioManager:
    """Manages a user's stock portfolio."""

    def __init__(self):
        self.holdings: Dict[str, int] = {}

    def update_portfolio(self, symbol: str, quantity: int, is_buy: bool):
        if is_buy:
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        else:
            if symbol in self.holdings:
                self.holdings[symbol] = max(0, self.holdings[symbol] - quantity)

    def get_portfolio_summary(self) -> str:
        summary = "Current Portfolio:\n"
        for symbol, quantity in self.holdings.items():
            summary += f"  {symbol}: {quantity} shares\n"
        return summary


class EnhancedTradingFacade(TradingFacade):
    """Enhanced facade that includes portfolio management."""

    def __init__(self):
        super().__init__()
        self.portfolio_manager = PortfolioManager()

    def analyze_and_trade(self, symbol: str, quantity: int):
        price = self.exchange.get_price(symbol)
        if price == 0.0:
            print(f"Error: Stock {symbol} not found")
            return

        # Analyze risk
        risk_level = self.risk_analyzer.analyze_risk(symbol, quantity)
        print(f"Risk level for this trade: {risk_level}")

        # Decide whether to buy or sell
        if self.trading_bot.should_buy(symbol, price):
            action = "buy"
        elif self.trading_bot.should_sell(symbol, price):
            action = "sell"
        else:
            print("No action recommended by the trading bot")
            return

        # Execute trade
        success = self.exchange.execute_trade(symbol, quantity, action == "buy")
        if success:
            self.logger.log_trade(symbol, quantity, price, action == "buy")
            self.portfolio_manager.update_portfolio(symbol, quantity, action == "buy")

            # Calculate and report taxes (assuming a profit for simplicity)
            profit = quantity * price * 0.1  # Assume 10% profit
            tax = self.tax_calculator.calculate_tax(profit)
            print(f"Estimated tax on profit: ${tax:.2f}")

            # Display updated portfolio
            print(self.portfolio_manager.get_portfolio_summary())
        else:
            print("Trade execution failed")


def run_enhanced_trading_simulation():
    """Simulate trading operations using the EnhancedTradingFacade."""
    facade = EnhancedTradingFacade()

    print("Scenario 1: Buying AAPL")
    facade.analyze_and_trade("AAPL", 10)

    print("\nScenario 2: Buying GOOGL")
    facade.analyze_and_trade("GOOGL", 5)

    print("\nScenario 3: Selling some AAPL")
    facade.analyze_and_trade("AAPL", 3)

    print("\nScenario 4: Buying MSFT")
    facade.analyze_and_trade("MSFT", 15)

    print("\nScenario 5: Attempting to trade an non-existent stock")
    facade.analyze_and_trade("INVALID", 100)


if __name__ == "__main__":
    print("Running basic trading simulation:")
    run_trading_simulation()

    print("\n" + "=" * 50 + "\n")

    print("Running enhanced trading simulation with portfolio management:")
    run_enhanced_trading_simulation()
