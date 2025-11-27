from dataclasses import dataclass
from typing import Optional
from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

@dataclass
class UserProfile:
    name: str
    email: str
    phone: str

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: int  # in cents
    external_url: Optional[str] = None

@dataclass
class Order:
    id: int
    product_id: int
    customer_principal: str
    customer_name: str
    shipping_address: str
    contact_info: str
    quantity: int
    status: OrderStatus
