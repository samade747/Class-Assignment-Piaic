# control_and_functions.py

# -----------------------------
# 1. Conditional Statements
# -----------------------------

print("🔸 Conditional Statements")

x = 10
if x > 5:
    print("x is greater than 5")

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

x = 5
if x > 5:
    print("Greater than 5")
elif x == 5:
    print("Equal to 5")
else:
    print("Less than 5")

print("\n")

# -----------------------------
# 2. Looping Statements
# -----------------------------

print("🔸 For Loop")
for i in range(5):
    print(i)

print("\n🔸 While Loop")
count = 0
while count < 5:
    print(count)
    count += 1

print("\n🔸 Break Example")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\n🔸 Continue Example")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\n")

# -----------------------------
# 3. Functions
# -----------------------------

print("🔸 Functions")

def greet():
    print("Hello, world!")

greet()

def greet_person(name):
    print("Hello,", name)

greet_person("Alice")

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

print("\n🔸 bin() function example")
x = 10
print("Binary of 10:", bin(x))
