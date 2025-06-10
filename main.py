from models import PricingRule
from controller import Checkout

if __name__ == "__main__":
    pricing_rules = [
        PricingRule('A', 50, 3, 130),  # 50 each, 3 for 130
        PricingRule('B', 30, 2, 45),   # 30 each, 2 for 45
        PricingRule('C', 20),          # 20 each, no bulk pricing
        PricingRule('D', 15)           # 15 each, no bulk pricing
    ]

    checkout = Checkout(pricing_rules)

    print("Enter items (e.g., 'ABCD').")
    while True:
        items = input("Input: ").strip()
        # this will calculate and show the total price
        total = checkout.calculate_total(items)
        print(f"Input: '{items}' => Total: {total}")