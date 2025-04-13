# Logical Operators in Python 🧠

This example demonstrates the use of **logical operators** in Python with real-life scenarios like login authentication and discount eligibility.

## 🔧 Operators Covered

| Operator | Description                                  | Example               |
|----------|----------------------------------------------|-----------------------|
| `and`    | True if **both** conditions are True         | `A and B`             |
| `or`     | True if **any one** condition is True        | `A or B`              |
| `not`    | Reverses the result (True ↔ False)           | `not A`               |

---

## 🧪 Example 1: Login Check

```python
is_logged_in = (input_username == username) and (input_password == password)
