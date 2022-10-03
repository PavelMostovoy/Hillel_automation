import time

start = time.time()

class OurBilling:
    _order_numbers = []
    __allowed_types = ["apple", "orange", "calculator"]

    def __init__(self, order_number: int, quality: int, total_price: float):
        if order_number in self._order_numbers:
            order_number += time.time() - start
        self._order_numbers.append(order_number)
        self.order_number = order_number
        self.quality = quality
        self.total_price = total_price
        self.__product_type = "default"

    def get_order_numbers(self):
        return self._order_numbers

    def price_per_item(self):
        price_per_item = self.total_price / self.quality
        return price_per_item

    def representation(self):
        print(self.__product_type)
        print(self.quality)

    @property
    def product_type(self):
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        if type(value) == str:
            if value in self.__allowed_types:
                self.__product_type = value
            else:
                raise IndexError

        else:
            raise ValueError("incorrect type")

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

print(third.price_per_item())

print(first.product_type)
first.product_type = "Apple"
print(first.product_type)
