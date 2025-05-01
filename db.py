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