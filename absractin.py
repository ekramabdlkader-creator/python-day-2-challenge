
from abc import ABC, abstractmethod


# 1. Define the Abstract Base Class (The Blueprint)
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        # This is an abstract method. It has no body.
        # It forces all child classes to create their own version of this.
        pass


# 2. Create a Child Class for Credit Card
class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")


# 3. Create a Child Class for PayPal
class PayPal(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


# --- Execution ---

# p = Payment()  <-- This would throw an ERROR because Payment is abstract.

obj1 = CreditCard()
obj1.process_payment(100)

obj2 = PayPal()
obj2.process_payment(50)

