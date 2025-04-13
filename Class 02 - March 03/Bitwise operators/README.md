# Bitwise Operators in Python

## 🧠 What are Bitwise Operators?
Bitwise operators perform operations on binary representations of integers. These are used to manipulate bits directly.

## ✅ List of Bitwise Operators

Assume: `x = 10` (`1010` in binary), `y = 4` (`0100` in binary)

| Operator | Name            | Description                              | Example     | Result  | Binary Result |
|----------|------------------|------------------------------------------|-------------|---------|----------------|
| `&`      | AND              | Sets each bit to 1 if both bits are 1    | `x & y`     | `0`     | `0000`         |
| `|`      | OR               | Sets each bit to 1 if one of two bits is 1 | `x \| y`   | `14`    | `1110`         |
| `^`      | XOR              | Sets each bit to 1 if only one bit is 1  | `x ^ y`     | `14`    | `1110`         |
| `~`      | NOT              | Inverts all the bits                     | `~x`        | `-11`   | (Two's complement) |
| `<<`     | Left Shift       | Shifts bits to the left by specified number of positions | `x << 2` | `40` | `101000`       |
| `>>`     | Right Shift      | Shifts bits to the right by specified number of positions | `x >> 2` | `2`  | `0010`         |
