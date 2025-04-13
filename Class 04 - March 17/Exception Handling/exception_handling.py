# exception_handling.py

# ---------------------------------
# 1. Basic try-except block
# ---------------------------------

print("🔹 Basic try-except block")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Oops! That's not a valid number.")

print("\n")

# ---------------------------------
# 2. Handling multiple exceptions
# ---------------------------------

print("🔹 Handling multiple exceptions")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

print("\n")

# ---------------------------------
# 3. try-except-else-finally
# ---------------------------------

print("🔹 try-except-else-finally")

try:
    n = int(input("Enter a number: "))
except ValueError:
    print("That’s not a number!")
else:
    print("Success! You entered:", n)
finally:
    print("This block always runs.")

print("\n")

# ---------------------------------
# 4. Raising custom exceptions
# ---------------------------------

print("🔹 Raising and handling custom exceptions")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Valid age:", age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
