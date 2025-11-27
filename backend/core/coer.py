from typing import Dict, List, Optional
from models.models import UserProfile, Product, Order, OrderStatus
from access.access_control import AccessControl, UserRole

class LTEFoodsBackend:
    def __init__(self):
        self.access_control = AccessControl()
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}
        self.user_profiles: Dict[str, UserProfile] = {}
        self.next_product_id = 0
        self.next_order_id = 0
        self._initialize_default_products()
    
    def _initialize_default_products(self):
        if not self.products:
            humble_pie = Product(
                id=self.next_product_id,
                name="Humble Pie",
                description="A delicious slice of humility, perfect for any occasion. Send to friends, family, or enemies!",
                price=1999,
                external_url="https://example-bakery.com/humble-pie"
            )
            self.products[self.next_product_id] = humble_pie
            self.next_product_id += 1
            
            tallest_pile = Product(
                id=self.next_product_id,
                name="Tallest Pile of Shit",
                description="A tongue-in-cheek gift for those who love to talk big. Comes with a certificate of authenticity.",
                price=2999
            )
            self.products[self.next_product_id] = tallest_pile
            self.next_product_id += 1
            
            high_proof_pudding = Product(
                id=self.next_product_id,
                name="High Proof Pudding",
                description="A boozy dessert for those who like their sweets with a kick. Must be 21+ to order.",
                price=2499,
                external_url="https://example-distillery.com/high-proof-pudding"
            )
            self.products[self.next_product_id] = high_proof_pudding
            self.next_product_id += 1
    
    # Access control wrappers
    def initialize_access_control(self, caller: str) -> None:
        self.access_control.initialize(caller)
    
    def get_caller_user_role(self, caller: str) -> UserRole:
        return self.access_control.get_user_role(caller)
    
    def assign_caller_user_role(self, caller: str, user: str, role: UserRole) -> None:
        self.access_control.assign_role(caller, user, role)
    
    def is_caller_admin(self, caller: str) -> bool:
        return self.access_control.is_admin(caller)
    
    # User profiles
    def get_caller_user_profile(self, caller: str) -> Optional[UserProfile]:
        if not self.access_control.has_permission(caller, UserRole.USER):
            raise Exception("Unauthorized")
        return self.user_profiles.get(caller)
    
    def save_caller_user_profile(self, caller: str, profile: UserProfile) -> None:
        if not self.access_control.has_permission(caller, UserRole.USER):
            raise Exception("Unauthorized")
        self.user_profiles[caller] = profile
    
    # Products
    def get_products(self) -> List[Product]:
        return list(self.products.values())
    
    def get_product(self, product_id: int) -> Optional[Product]:
        return self.products.get(product_id)
    
    # Orders
    def place_order(
        self, caller: str, product_id: int, customer_name: str,
        shipping_address: str, contact_info: str, quantity: int
    ) -> int:
        if not self.access_control.has_permission(caller, UserRole.USER):
            raise Exception("Unauthorized")
        if product_id not in self.products:
            raise Exception("Product not found")
        order = Order(
            id=self.next_order_id,
            product_id=product_id,
            customer_principal=caller,
            customer_name=customer_name,
            shipping_address=shipping_address,
            contact_info=contact_info,
            quantity=quantity,
            status=OrderStatus.PENDING
        )
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order.id
