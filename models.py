class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PricingRule:
    def __init__(self, item, unit_price, bulk_qty=None, bulk_price=None):
        self.item = item  # 'A', 'B'
        self.unit_price = unit_price 
        self.bulk_qty = bulk_qty  # Quantity for bulk discount
        self.bulk_price = bulk_price  # Price for bulk quantity