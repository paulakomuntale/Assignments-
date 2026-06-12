# ============================================
# E-COMMERCE SYSTEM
# Assignment 2 - Control Structures
# ============================================

print("===================================")
print("      E-COMMERCE LOGIN SYSTEM      ")
print("===================================")

# ----------------------
# LOGIN SYSTEM
# ----------------------

username = input("Enter Username: ")
password = input("Enter Password: ")

# Default role
role = ""

# User Authentication
if username == "admin" and password == "admin123":
    role = "Admin"

elif username == "customer" and password == "cust123":
    role = "Customer"

elif username == "cashier" and password == "cash123":
    role = "Cashier"

else:
    print("Invalid Username or Password")
    exit()

# ----------------------
# ACCESS LEVELS
# ----------------------

print("\nLogin Successful")
print("Role:", role)

if role == "Admin":
    print("Access Level: Full System Access")

elif role == "Cashier":
    print("Access Level: Billing and Sales")

elif role == "Customer":
    print("Access Level: Shopping Features")

# ----------------------
# E-COMMERCE CHECKOUT
# ----------------------

print("\n===================================")
print("         PRODUCT CHECKOUT          ")
print("===================================")

subtotal = float(input("Enter Product Subtotal: "))

# ----------------------
# DISCOUNT LEVELS
# ----------------------

if subtotal >= 1000:
    discount_rate = 20
elif subtotal >= 500:
    discount_rate = 10
elif subtotal >= 200:
    discount_rate = 5
else:
    discount_rate = 0

discount_amount = subtotal * discount_rate / 100

print("Discount Rate:", discount_rate, "%")
print("Discount Amount:", discount_amount)

# ----------------------
# COUPON VALIDATION
# ----------------------

coupon_code = input("Enter Coupon Code: ")

coupon_discount = 0

if coupon_code == "SAVE10":
    coupon_discount = subtotal * 0.10
    print("Valid Coupon Applied (10%)")

elif coupon_code == "SAVE20":
    coupon_discount = subtotal * 0.20
    print("Valid Coupon Applied (20%)")

elif coupon_code == "SAVE30":
    coupon_discount = subtotal * 0.30
    print("Valid Coupon Applied (30%)")

else:
    print("Invalid Coupon Code")

# ----------------------
# PRICE AFTER DISCOUNTS
# ----------------------

price_after_discount = (
    subtotal
    - discount_amount
    - coupon_discount
)

# ----------------------
# LOCATION TAX RATE
# ----------------------

location = input(
    "Enter Location (Uganda/Kenya/Tanzania): "
)

if location.lower() == "uganda":
    tax_rate = 18

elif location.lower() == "kenya":
    tax_rate = 16

elif location.lower() == "tanzania":
    tax_rate = 15

else:
    tax_rate = 10

tax_amount = (
    price_after_discount
    * tax_rate / 100
)

# ----------------------
# FINAL PRICE
# ----------------------

final_price = (
    price_after_discount
    + tax_amount
)

# ----------------------
# RECEIPT
# ----------------------

print("\n===================================")
print("            RECEIPT                ")
print("===================================")

print(f"Subtotal:          {subtotal:.2f}")
print(f"Discount:          {discount_amount:.2f}")
print(f"Coupon Discount:   {coupon_discount:.2f}")
print(f"Tax Amount:        {tax_amount:.2f}")
print(f"Final Price:       {final_price:.2f}")

print("===================================")
print("Thank You For Shopping!")
print("===================================")