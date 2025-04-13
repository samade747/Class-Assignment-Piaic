# math_datetime_calendar.py

import math
import datetime
import calendar

# -----------------------------
# 📐 Math Module
# -----------------------------

print("🔸 Math Module Examples")

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("Factorial of 5:", math.factorial(5))
print("Power (2^3):", math.pow(2, 3))
print("Cosine of 0:", math.cos(0))
print("Log base 10 of 1000:", math.log10(1000))

print("\n")

# -----------------------------
# 🕒 datetime Module
# -----------------------------

print("🔸 datetime Module Examples")

now = datetime.datetime.now()
print("Current Date & Time:", now)

today = datetime.date.today()
print("Today's Date:", today)

custom_date = datetime.date(2025, 4, 13)
print("Custom Date:", custom_date)

# Time difference
future = datetime.date(2025, 12, 25)
delta = future - today
print("Days until Christmas 2025:", delta.days)

# Format datetime
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("Formatted DateTime:", formatted)

print("\n")

# -----------------------------
# 📅 calendar Module
# -----------------------------

print("🔸 Calendar Module Examples")

# Display a calendar for a month
print("Calendar for April 2025:")
print(calendar.month(2025, 4))

# Display full year calendar
print("Full Calendar for 2025:")
print(calendar.calendar(2025))

# Check if a year is a leap year
print("Is 2024 a leap year?", calendar.isleap(2024))
print("Is 2025 a leap year?", calendar.isleap(2025))
