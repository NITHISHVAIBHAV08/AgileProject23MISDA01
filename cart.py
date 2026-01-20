# cart.py

cart = []

def add_to_cart(product_name, price):
    cart.append({"product": product_name, "price": price})
    print(f"{product_name} added to cart")

def view_cart():
    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(item["product"], "-", item["price"])
        total += item["price"]
    print("Total Amount:", total)

add_to_cart("Laptop", 60000)
view_cart()
