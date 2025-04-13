# logical.py

# Logical Operators in Python: and, or, not

# Example: Checking login and discount eligibility

# User information
username = "sam123"
password = "secret"

# Login input
input_username = "sam123"
input_password = "secret"

# 1. AND operator: both username and password must match
is_logged_in = (input_username == username) and (input_password == password)
print("Login successful:", is_logged_in)

# Example 2: Discount eligibility
is_student = True
has_coupon = False

# 2. OR operator: if user is a student OR has a coupon, they get discount
gets_discount = is_student or has_coupon
print("Eligible for discount:", gets_discount)

# 3. NOT operator: if NOT eligible, show message
print("Not eligible for discount:", not gets_discount)
