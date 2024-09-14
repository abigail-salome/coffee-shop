import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_name_valid():
    customer = Customer("Alice")
    assert customer.name == "Alice"


def test_customer_name_invalid_empty():
    with pytest.raises(TypeError):
        Customer("")


def test_customer_name_invalid_long():
    with pytest.raises(TypeError):
        Customer("ThisNameIsWayTooLong")


def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
