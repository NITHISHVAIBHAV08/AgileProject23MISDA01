# product_service.py

products = [
    {"id": 1, "name": "Laptop", "price": 60000},
    {"id": 2, "name": "Smartphone", "price": 30000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

def display_products():
    print("\nAvailable Products:")
    for product in products:
        print(f"{product['id']}. {product['name']} - Rs.{product['price']}")

display_products()
