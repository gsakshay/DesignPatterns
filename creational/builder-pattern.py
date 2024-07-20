from __future__ import annotations
from typing import List, Optional


class Asset:
    def __init__(self, name: str, allocation: float):
        self.name = name
        self.allocation = allocation


class InvestmentPortfolio:
    def __init__(self):
        self.name: str = ""
        self.risk_level: str = ""
        self.assets: List[Asset] = []
        self.rebalance_frequency: str = ""
        self.tax_optimization: bool = False

    def __str__(self) -> str:
        assets_str = ", ".join([f"{asset.name} ({asset.allocation}%)" for asset in self.assets])
        return (f"Portfolio: {self.name}\n"
                f"Risk Level: {self.risk_level}\n"
                f"Assets: {assets_str}\n"
                f"Rebalance Frequency: {self.rebalance_frequency}\n"
                f"Tax Optimization: {'Enabled' if self.tax_optimization else 'Disabled'}")


class InvestmentPortfolioBuilder:
    def __init__(self):
        self.portfolio = InvestmentPortfolio()

    def set_name(self, name: str) -> InvestmentPortfolioBuilder:
        self.portfolio.name = name
        return self

    def set_risk_level(self, risk_level: str) -> InvestmentPortfolioBuilder:
        self.portfolio.risk_level = risk_level
        return self

    def add_asset(self, name: str, allocation: float) -> InvestmentPortfolioBuilder:
        self.portfolio.assets.append(Asset(name, allocation))
        return self

    def set_rebalance_frequency(self, frequency: str) -> InvestmentPortfolioBuilder:
        self.portfolio.rebalance_frequency = frequency
        return self

    def enable_tax_optimization(self) -> InvestmentPortfolioBuilder:
        self.portfolio.tax_optimization = True
        return self

    def build(self) -> InvestmentPortfolio:
        return self.portfolio


class InvestmentAdvisor:
    @staticmethod
    def create_conservative_portfolio() -> InvestmentPortfolio:
        return (InvestmentPortfolioBuilder()
                .set_name("Conservative Growth")
                .set_risk_level("Low")
                .add_asset("Government Bonds", 40)
                .add_asset("Blue-chip Stocks", 30)
                .add_asset("Investment Grade Corporate Bonds", 30)
                .set_rebalance_frequency("Annually")
                .build())

    @staticmethod
    def create_aggressive_portfolio() -> InvestmentPortfolio:
        return (InvestmentPortfolioBuilder()
                .set_name("Aggressive Growth")
                .set_risk_level("High")
                .add_asset("Small-cap Stocks", 40)
                .add_asset("Emerging Market Stocks", 30)
                .add_asset("Commodities", 20)
                .add_asset("High-yield Bonds", 10)
                .set_rebalance_frequency("Quarterly")
                .enable_tax_optimization()
                .build())


# Usage
if __name__ == "__main__":
    advisor = InvestmentAdvisor()

    conservative_portfolio = advisor.create_conservative_portfolio()
    print(conservative_portfolio)

    print("\n")

    aggressive_portfolio = advisor.create_aggressive_portfolio()
    print(aggressive_portfolio)

    # Custom portfolio
    custom_portfolio = (InvestmentPortfolioBuilder()
                        .set_name("Tech-focused Growth")
                        .set_risk_level("Medium-High")
                        .add_asset("Tech Sector ETF", 50)
                        .add_asset("AI and Robotics Fund", 30)
                        .add_asset("Cryptocurrency", 10)
                        .add_asset("Cash", 10)
                        .set_rebalance_frequency("Monthly")
                        .enable_tax_optimization()
                        .build())
    print("\n")
    print(custom_portfolio)