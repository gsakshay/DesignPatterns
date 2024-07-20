from abc import ABC, abstractmethod
from typing import Dict
import random


class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class ModernPaymentGateway(PaymentProcessor):
    """Modern payment gateway that processes payments directly."""

    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} through Modern Payment Gateway")
        return random.random() < 0.95  # 95% success rate


class LegacyPaymentSystem:
    """Legacy payment system with a different interface."""

    def initialize_payment(self, amount: float) -> str:
        print(f"Initializing payment of ${amount:.2f} in Legacy Payment System")
        return "PAYMENT_ID_" + str(random.randint(10000, 99999))

    def process_payment(self, payment_id: str) -> Dict[str, bool]:
        print(f"Processing payment {payment_id} in Legacy Payment System")
        success = random.random() < 0.9  # 90% success rate
        return {"status": success}


class LegacyPaymentAdapter(PaymentProcessor):
    """Adapter to make LegacyPaymentSystem compatible with PaymentProcessor interface."""

    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy_system = legacy_system

    def process_payment(self, amount: float) -> bool:
        payment_id = self.legacy_system.initialize_payment(amount)
        result = self.legacy_system.process_payment(payment_id)
        return result["status"]


class PaymentService:
    """Payment service that uses different payment processors."""

    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def make_payment(self, amount: float) -> bool:
        return self.payment_processor.process_payment(amount)


def run_payment_simulation():
    """Simulate payments using different payment systems."""
    modern_gateway = ModernPaymentGateway()
    legacy_system = LegacyPaymentSystem()
    legacy_adapter = LegacyPaymentAdapter(legacy_system)

    modern_service = PaymentService(modern_gateway)
    legacy_service = PaymentService(legacy_adapter)

    print("Processing payments through Modern Payment Gateway:")
    for _ in range(3):
        amount = random.uniform(10, 1000)
        success = modern_service.make_payment(amount)
        print(f"Payment of ${amount:.2f} {'successful' if success else 'failed'}")

    print("\nProcessing payments through Legacy Payment System (via Adapter):")
    for _ in range(3):
        amount = random.uniform(10, 1000)
        success = legacy_service.make_payment(amount)
        print(f"Payment of ${amount:.2f} {'successful' if success else 'failed'}")


if __name__ == "__main__":
    run_payment_simulation()
