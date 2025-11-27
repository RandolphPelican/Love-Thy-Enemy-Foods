from core.core import LTEFoodsBackend
from models.models import UserProfile

if __name__ == "__main__":
    backend = LTEFoodsBackend()
    
    # Initialize first caller as admin
    backend.initialize_access_control("user1")
    
    # Print products
    products = backend.get_products()
    print("Available products:")
    for product in products:
        print(f"- {product.name}: ${product.price / 100:.2f}")
    
    # Save a sample user profile
    profile = UserProfile(name="John Doe", email="john@example.com", phone="555-1234")
    backend.save_caller_user_profile("user1", profile)
    
    # Place an order for "Tallest Pile of Shit" (product_id = 1)
    order_id = backend.place_order(
        caller="user1",
        product_id=1,
        customer_name="John Doe",
        shipping_address="123 Main St, City, State, ZIP",
        contact_info="john@example.com",
        quantity=2
    )
    print(f"Order placed with ID: {order_id}")
