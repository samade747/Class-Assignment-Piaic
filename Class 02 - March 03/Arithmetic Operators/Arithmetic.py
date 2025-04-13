# Real-World Example: Grocery Billing System

# Prices of items
apple_price = 2   # $2 per apple
banana_price = 1  # $1 per banana

# Quantities bought
apples_bought = 4
bananas_bought = 6

# 1. Addition (Total bill)
total_bill = (apple_price * apples_bought) + (banana_price * bananas_bought)
print("Total bill is $", total_bill)

# 2. Subtraction (Discount applied)
discount = 3
final_bill = total_bill - discount
print("Final bill after $3 discount is $", final_bill)

# 3. Division (Split bill between 2 people)
split_amount = final_bill / 2
print("Each person pays $", split_amount)

# 4. Floor Division (Whole number of packets bought)
total_items = apples_bought + bananas_bought
packets = total_items // 5  # Suppose 1 packet holds 5 items
print("Total packets needed:", packets)

# 5. Modulus (Leftover items after making packets)
leftovers = total_items % 5
print("Leftover items after packing:", leftovers)

# 6. Exponentiation (Discount doubles every year)
years = 3
initial_discount = 1
future_discount = initial_discount ** years
print("Discount after 3 years will be $", future_discount)
