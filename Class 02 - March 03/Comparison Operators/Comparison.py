# You are buying a laptop
budget = 1000
laptop_price = 950

# 1. Check if it's within your budget
print("Can you buy it?", laptop_price <= budget)  # True

# 2. Check if you need more money
print("Do you need more money?", laptop_price > budget)  # False

# 3. Check if the laptop is exactly your budget
print("Perfect match?", laptop_price == budget)  # False

# 4. What if the laptop price is not equal to budget
print("Is price not equal to budget?", laptop_price != budget)  # True

# 5. Suppose you got a $50 discount
laptop_price -= 50
print("New price is $", laptop_price)

# 6. Can you buy now?
print("Can you buy after discount?", laptop_price <= budget)  # True
