import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
from coffee import Coffee
from order import Order
from customer import Customer


def test_coffee_name_valid():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"


def test_coffee_name_invalid():
    with pytest.raises(TypeError):
        Coffee("Ex")  # Less than 3 characters
