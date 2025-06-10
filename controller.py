from collections import Counter
from models import PricingRule

class Checkout:
    def __init__(self, pricing_rules):
       
        self.pricing_rules = {rule.item: rule for rule in pricing_rules}

    def calculate_total(self, items):
        total = 0
        item_counts = Counter(items)  # this basically count occurrences of each item

        for item, count in item_counts.items():
            rule = self.pricing_rules.get(item)
            if rule:
                if rule.bulk_qty and rule.bulk_price:
                    bulk_sets = count // rule.bulk_qty
                    remaining_items = count % rule.bulk_qty
                    total += (bulk_sets * rule.bulk_price) + (remaining_items * rule.unit_price)
                else:
                    #if no bulk pricing,it should calculate normally
                    total += count * rule.unit_price

        return total