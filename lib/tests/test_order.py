import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0


def test_order_invalid_customer():
    with pytest.raises(TypeError):
        Order("NotACustomer", Coffee("Espresso"), 5.0)


def test_order_invalid_coffee():
    with pytest.raises(TypeError):
        Order(Customer("Alice"), "NotACoffee", 5.0)


def test_order_invalid_price():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    with pytest.raises(TypeError):
        Order(customer, coffee, 0.5)  # Price less than 1.0
    with pytest.raises(TypeError):
        Order(customer, coffee, 20.0)  # Price greater than 10.0
