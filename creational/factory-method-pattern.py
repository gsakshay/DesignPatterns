from abc import ABC, abstractmethod
from typing import Dict, Any


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        # Simulate credit card processing logic
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        # Simulate PayPal processing logic
        return True


class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing cryptocurrency payment of ${amount}")
        # Simulate cryptocurrency processing logic
        return True


class PaymentProcessorFactory:
    @staticmethod
    def create_processor(payment_method: str) -> PaymentProcessor:
        if payment_method == "credit_card":
            return CreditCardProcessor()
        elif payment_method == "paypal":
            return PayPalProcessor()
        elif payment_method == "crypto":
            return CryptoProcessor()
        else:
            raise ValueError(f"Unsupported payment method: {payment_method}")


class PaymentService:
    def __init__(self, factory: PaymentProcessorFactory):
        self.factory = factory

    def process_payment(self, amount: float, payment_method: str) -> bool:
        processor = self.factory.create_processor(payment_method)
        return processor.process_payment(amount)


# Usage
if __name__ == "__main__":
    factory = PaymentProcessorFactory()
    payment_service = PaymentService(factory)

    # Process different types of payments
    payment_service.process_payment(100.00, "credit_card")
    payment_service.process_payment(50.00, "paypal")
    payment_service.process_payment(75.00, "crypto")
