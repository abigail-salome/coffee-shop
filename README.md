## Coffee Shop
This project is a simple Coffee Ordering System where users (customers) can place orders for different types of coffee. It consists of three main classes: Customer, Coffee, and Order. The system allows users to create orders, track the coffees ordered, and manage the price of each order.

#### Features
* Customer: A customer can place orders for different coffee types and view their orders.
* Coffee: Represents different coffee types. Each coffee has a name and a list of orders associated with it.
* Order: Tracks which customer placed the order, which coffee was ordered, and the price of the order.

#### Project Structure
project/
│
├── coffee.py            # Coffee class
├── customer.py          # Customer class
├── order.py             # Order class
├── tests/
│   ├── test_coffee.py   # Pytest test cases for Coffee class
│   ├── test_customer.py # Pytest test cases for Customer class
│   └── test_order.py    # Pytest test cases for Order class
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

#### Requirements
Python 3.12.3 or later
pytest for running unit tests

#### installation
1. Clone the repository:
2. git clone https://github.com/abigail-salome/coffee-shop
3. cd coffee-ordering-system
4. Create a virtual environment:
5. python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

#### Install dependencies:
* pip install -r requirements.txt

#### Usage
1. Creating a Coffee:
* from coffee import Coffee
* espresso = Coffee("Espresso")
* print(espresso.name) 

2. Creating a Customer:
* from customer import Customer
* alice = Customer("Alice")
* print(alice.name)  # Output: Alice

3. Placing an Order:
* from order import Order
* from customer import Customer
* from coffee import Coffee
* customer = Customer("Alice")
* coffee = Coffee("Espresso")
* order = Order(customer, coffee, 5.0)
print(order.customer.name)  
print(order.coffee.name)    
print(order.price)     

#### Running Tests
You can run the test cases using pytest:
1. Navigate to the project directory:
2. cd project
3. Run all test using this command:pytest

The tests will ensure that:
1. Valid coffee and customer names are handled correctly.
2. Orders are created properly.
3. Invalid inputs (e.g., wrong price ranges) raise errors as expected.
