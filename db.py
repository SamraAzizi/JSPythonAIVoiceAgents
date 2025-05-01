from typing import Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    order_number: str
    customer_name: str
    items: list
    total_amount: float
    order_date: datetime
    status: str
    shipping_address: str

    orders_db: Dict[str, Order] = {
    "101": Order(
        order_number="101",
        customer_name="John Doe",
        items=[
            {"product": "Laptop", "quantity": 1, "price": 999.99},
            {"product": "Mouse", "quantity": 1, "price": 29.99}
        ],