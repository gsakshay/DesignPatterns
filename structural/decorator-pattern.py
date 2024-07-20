from abc import ABC, abstractmethod
from typing import List


class InvestmentAccount(ABC):
    """Abstract base class for investment accounts."""

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class BasicInvestmentAccount(InvestmentAccount):
    """Basic investment account implementation."""

    def __init__(self, initial_balance: float = 0):
        self._balance = initial_balance

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_description(self) -> str:
        return "Basic Investment Account"


class InvestmentAccountDecorator(InvestmentAccount):
    """Base decorator class for investment accounts."""

    def __init__(self, account: InvestmentAccount):
        self._account = account

    def get_balance(self) -> float:
        return self._account.get_balance()

    def deposit(self, amount: float) -> None:
        self._account.deposit(amount)

    def withdraw(self, amount: float) -> None:
        self._account.withdraw(amount)

    def get_description(self) -> str:
        return self._account.get_description()


class InsuranceDecorator(InvestmentAccountDecorator):
    """Decorator that adds insurance to an investment account."""

    def __init__(self, account: InvestmentAccount, coverage_limit: float):
        super().__init__(account)
        self._coverage_limit = coverage_limit

    def get_description(self) -> str:
        return f"{self._account.get_description()} + Insurance (up to ${self._coverage_limit:.2f})"

    def claim_insurance(self, amount: float) -> float:
        claim_amount = min(amount, self._coverage_limit)
        print(f"Insurance claim: ${claim_amount:.2f}")
        return claim_amount


class TaxAdvantageDecorator(InvestmentAccountDecorator):
    """Decorator that adds tax advantages to an investment account."""

    def __init__(self, account: InvestmentAccount, tax_rate: float):
        super().__init__(account)
        self._tax_rate = tax_rate

    def get_description(self) -> str:
        return f"{self._account.get_description()} + Tax Advantage ({self._tax_rate * 100:.1f}% rate)"

    def withdraw(self, amount: float) -> None:
        taxed_amount = amount * (1 - self._tax_rate)
        super().withdraw(taxed_amount)
        print(f"Tax-advantaged withdrawal: ${amount:.2f} (${taxed_amount:.2f} after tax)")


class RoboAdvisorDecorator(InvestmentAccountDecorator):
    """Decorator that adds robo-advisor features to an investment account."""

    def __init__(self, account: InvestmentAccount):
        super().__init__(account)
        self._portfolio: List[str] = []

    def get_description(self) -> str:
        return f"{self._account.get_description()} + Robo-Advisor"

    def rebalance_portfolio(self) -> None:
        print("Rebalancing portfolio based on market conditions and risk profile")
        self._portfolio = ["ETF_A", "ETF_B", "BOND_X", "STOCK_Y"]

    def get_investment_advice(self) -> str:
        return "Based on your profile, consider increasing your bond allocation."


def create_premium_account(initial_balance: float) -> InvestmentAccount:
    """Create a premium investment account with multiple features."""
    basic_account = BasicInvestmentAccount(initial_balance)
    insured_account = InsuranceDecorator(basic_account, 50000)
    tax_advantaged_account = TaxAdvantageDecorator(insured_account, 0.15)
    premium_account = RoboAdvisorDecorator(tax_advantaged_account)
    return premium_account


def demonstrate_account_operations(account: InvestmentAccount):
    """Demonstrate operations on the given investment account."""
    print(f"\nAccount type: {account.get_description()}")
    print(f"Initial balance: ${account.get_balance():.2f}")

    account.deposit(10000)
    print(f"After $10,000 deposit: ${account.get_balance():.2f}")

    account.withdraw(3000)
    print(f"After $3,000 withdrawal: ${account.get_balance():.2f}")

    if isinstance(account, InsuranceDecorator):
        account.claim_insurance(5000)

    if isinstance(account, RoboAdvisorDecorator):
        account.rebalance_portfolio()
        advice = account.get_investment_advice()
        print(f"Robo-advisor says: {advice}")


if __name__ == "__main__":
    basic_account = BasicInvestmentAccount(5000)
    demonstrate_account_operations(basic_account)

    premium_account = create_premium_account(5000)
    demonstrate_account_operations(premium_account)
