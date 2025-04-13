# membership.py

# Membership Operators in Python: in, not in

# Shopping cart items
shopping_cart = ['apple', 'banana', 'cherry', 'date']

# 1. Check if an item is in the cart
item = 'apple'
print(f"Is {item} in the cart?", item in shopping_cart)  # True

# 2. Check if an item is not in the cart
item = 'grape'
print(f"Is {item} not in the cart?", item not in shopping_cart)  # True

# 3. Check if a letter is in a string (e.g., checking letters in a word)
word = "apple"
letter = 'p'
print(f"Is {letter} in {word}?", letter in word)  # True

# 4. Check if a letter is not in a string
letter = 'z'
print(f"Is {letter} not in {word}?", letter not in word)  # True
