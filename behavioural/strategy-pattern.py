from abc import ABC, abstractmethod
from typing import List, Dict
import random


class InvestmentStrategy(ABC):
    """Abstract base class for investment strategies."""

    @abstractmethod
    def allocate(self, portfolio: Dict[str, float], amount: float) -> Dict[str, float]:
        """
        Allocate the given amount across the portfolio according to the strategy.
        
        :param portfolio: Current portfolio allocation
        :param amount: Amount to invest
        :return: Dictionary of additional allocations
        """
        pass


class ConservativeStrategy(InvestmentStrategy):
    """A conservative investment strategy focusing on bonds and stable assets."""

    def allocate(self, portfolio: Dict[str, float], amount: float) -> Dict[str, float]:
        return {
            "Bonds": amount * 0.6,
            "Blue Chip Stocks": amount * 0.3,
            "Cash": amount * 0.1
        }


class AggressiveStrategy(InvestmentStrategy):
    """An aggressive investment strategy focusing on growth stocks and emerging markets."""

    def allocate(self, portfolio: Dict[str, float], amount: float) -> Dict[str, float]:
        return {
            "Growth Stocks": amount * 0.5,
            "Emerging Markets": amount * 0.3,
            "Cryptocurrencies": amount * 0.2
        }


class BalancedStrategy(InvestmentStrategy):
    """A balanced investment strategy aiming for moderate growth and risk."""

    def allocate(self, portfolio: Dict[str, float], amount: float) -> Dict[str, float]:
        return {
            "Index Funds": amount * 0.4,
            "Bonds": amount * 0.3,
            "Real Estate": amount * 0.2,
            "Cash": amount * 0.1
        }


class InvestmentPortfolio:
    """Represents an investment portfolio that can use different investment strategies."""

    def __init__(self, initial_balance: float = 0):
        self.balance = initial_balance
        self.holdings: Dict[str, float] = {}
        self.strategy: InvestmentStrategy = BalancedStrategy()  # Default strategy

    def set_strategy(self, strategy: InvestmentStrategy):
        """Change the investment strategy."""
        self.strategy = strategy

    def invest(self, amount: float):
        """Invest a given amount using the current strategy."""
        if amount > self.balance:
            amount = self.balance

        allocation = self.strategy.allocate(self.holdings, amount)
        for asset, value in allocation.items():
            if asset in self.holdings:
                self.holdings[asset] += value
            else:
                self.holdings[asset] = value
        
        self.balance -= amount

    def __str__(self):
        portfolio_str = f"Current Balance: ${self.balance:.2f}\n"
        portfolio_str += "Holdings:\n"
        for asset, value in self.holdings.items():
            portfolio_str += f"  {asset}: ${value:.2f}\n"
        return portfolio_str


class MarketSimulator:
    """Simulates market movements to adjust portfolio values."""

    @staticmethod
    def simulate_market_movement(portfolio: InvestmentPortfolio):
        """Simulate market movement and adjust portfolio values."""
        for asset in portfolio.holdings:
            # Random market movement between -5% and +5%
            movement = random.uniform(-0.05, 0.05)
            portfolio.holdings[asset] *= (1 + movement)


def run_investment_simulation(initial_balance: float, num_months: int):
    """Run an investment simulation over a specified number of months."""
    portfolio = InvestmentPortfolio(initial_balance)
    simulator = MarketSimulator()

    strategies = [
        ("Balanced", BalancedStrategy()),
        ("Conservative", ConservativeStrategy()),
        ("Aggressive", AggressiveStrategy())
    ]

    print(f"Starting investment simulation with ${initial_balance:.2f}")

    for month in range(1, num_months + 1):
        print(f"\nMonth {month}:")

        # Switch strategy every 3 months
        if month % 3 == 1:
            strategy_name, strategy = strategies[(month // 3) % len(strategies)]
            portfolio.set_strategy(strategy)
            print(f"Switching to {strategy_name} strategy")

        # Simulate monthly investment
        monthly_investment = 1000  # Fixed monthly investment
        portfolio.invest(monthly_investment)

        # Simulate market movement
        simulator.simulate_market_movement(portfolio)

        print(portfolio)


if __name__ == "__main__":
    run_investment_simulation(10000, 12)  # Start with $10,000 and simulate for 12 months
