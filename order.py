from coffee import Coffee
from customer import Customer


class Order:
    all_coffee = []
    all_customer = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_coffee.append(coffee)
        Order.all_customer.append(customer)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer class")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee class")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) or value < 1.0 or value > 10.0:
            raise TypeError("Enter a valid price")
        self._price = value
