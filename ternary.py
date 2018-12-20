#!/usr/bin/env python3

#ternary positive
hungry=True
x='Feed' if hungry else 'DONT Feed'
print(x)
#ternary negative
hungry=0
x='Feed' if hungry else 'DONT Feed'
print(x)
# ternary omit else
hungry=False
x='Feed' if hungry else None
print(x)