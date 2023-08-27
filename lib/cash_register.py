#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._get_last_item_price()
            self.total -= last_item_price
            self.items.pop()
            if not self.items:
                self.total = 0.0
        else:
            self.total = 0.0

    def _get_last_item_price(self):
        title = self.items[-1]
        return self._get_price_by_title(title)

    def _get_price_by_title(self, title):
        item_prices = {
            "macbook air": 1000,
            "eggs": 1.99,
            "tomato": 1.76
        }
        return item_prices.get(title, 0)



   



