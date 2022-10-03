import time

start = time.time()


class OurBilling:
    _order_numbers = []

    def __init__(self, order_number: int, quality: int, total_price: float):
        if order_number in self._order_numbers:
            order_number += time.time() - start
        self._order_numbers.append(order_number)
        self.order_number = order_number
        self.product_type = "staff"
        self.quality = quality
        self.total_price = total_price

    def get_order_numbers(self):
        return self._order_numbers


# order number
# product type
# quality
# overall price
#
# available or not
# actual amount
# return price to item


first = OurBilling(0, 2, 200.0)
second = OurBilling(1, 3, 150.0)
third = OurBilling(0, 2, 6.6)
first.order_numbers = [1, 2, 3, 4]
print(first.order_numbers)
five = OurBilling(0, 0, 0.0)
print(first.get_order_numbers())
