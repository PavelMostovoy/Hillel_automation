class OurBilling:
    def __init__(self, order_number: int, quantity: int, total_price: float):
        self.order_number = order_number
        self.product_type = "stuff"
        self.quantity = quantity
        self.total_price = total_price


# order number
# product type
# quantity
# total price

# available or not
# actual amount
# return price per item


first = OurBilling(0, 2, 200.0)
print(first.order_number)

second = OurBilling(1, 3, 150.0)
print(second.order_number)
