from __future__ import annotations
from typing import Dict, Optional
import threading
import time
import random


class ExchangeRateManager:
    _instance: Optional[ExchangeRateManager] = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self):
        self._rates: Dict[str, float] = {}
        self._last_updated: float = 0
        self._update_interval: int = 3600  # Update every hour

    @classmethod
    def get_instance(cls) -> ExchangeRateManager:
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        self._update_rates_if_needed()
        key = f"{from_currency}_{to_currency}"
        return self._rates.get(key, 1.0)

    def _update_rates_if_needed(self):
        current_time = time.time()
        if current_time - self._last_updated > self._update_interval:
            self._update_rates()

    def _update_rates(self):
        print("Updating exchange rates...")
        # In a real-world scenario, this would call an external API
        # Here, we're simulating with random fluctuations
        base_rates = {
            "USD_EUR": 0.85,
            "USD_GBP": 0.75,
            "USD_JPY": 110.0,
            "EUR_GBP": 0.88,
            "EUR_JPY": 129.5,
            "GBP_JPY": 146.7
        }

        for pair, rate in base_rates.items():
            fluctuation = random.uniform(-0.02, 0.02)  # +/- 2% fluctuation
            self._rates[pair] = rate * (1 + fluctuation)
            reverse_pair = f"{pair.split('_')[1]}_{pair.split('_')[0]}"
            self._rates[reverse_pair] = 1 / self._rates[pair]

        self._last_updated = time.time()


class CurrencyConverter:
    def __init__(self):
        self.rate_manager = ExchangeRateManager.get_instance()

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rate = self.rate_manager.get_rate(from_currency, to_currency)
        return amount * rate


# Usage
if __name__ == "__main__":
    converter1 = CurrencyConverter()
    converter2 = CurrencyConverter()

    print(f"Converter 1 id: {id(converter1.rate_manager)}")
    print(f"Converter 2 id: {id(converter2.rate_manager)}")
    print(f"Are the rate managers the same object? {converter1.rate_manager is converter2.rate_manager}")

    print("\nPerforming conversions:")
    amount = 1000
    print(f"{amount} USD to EUR: {converter1.convert(amount, 'USD', 'EUR'):.2f}")
    print(f"{amount} EUR to GBP: {converter1.convert(amount, 'EUR', 'GBP'):.2f}")
    print(f"{amount} GBP to JPY: {converter2.convert(amount, 'GBP', 'JPY'):.2f}")

    print("\nWaiting for rates to update...")
    time.sleep(2)  # Wait for rates to potentially update

    print("\nPerforming conversions again:")
    print(f"{amount} USD to EUR: {converter1.convert(amount, 'USD', 'EUR'):.2f}")
    print(f"{amount} EUR to GBP: {converter1.convert(amount, 'EUR', 'GBP'):.2f}")
    print(f"{amount} GBP to JPY: {converter2.convert(amount, 'GBP', 'JPY'):.2f}")