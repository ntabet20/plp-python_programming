# Week 3 Assignment
# 1. Function that calculates the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (20 / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# 2. Calling the function
price = int(input("Enter the price of item: "))
discount_percent = int(input("Enter the percentage discount: "))

print(calculate_discount(price, discount_percent))