# offers.py

def apply_discount(amount):
    discount = amount * 0.10
    final_price = amount - discount
    print("Discount Applied: Rs.", discount)
    print("Final Price:", final_price)

apply_discount(50000)
