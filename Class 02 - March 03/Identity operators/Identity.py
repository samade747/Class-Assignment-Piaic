# Identity Operators in Python 🔍

This example demonstrates the use of **identity operators** in Python. These operators check if two variables refer to the **same object** in memory.

## 🔧 Operators Covered

| Operator | Description                                      | Example                |
|----------|--------------------------------------------------|------------------------|
| `is`     | Returns `True` if both variables refer to the same object | `a is b`              |
| `is not` | Returns `True` if both variables **do not** refer to the same object | `a is not b`          |

---

## 🧪 Example 1: Same Object in Memory

```python
a = [1, 2, 3]
b = a
print(a is b)  # True
