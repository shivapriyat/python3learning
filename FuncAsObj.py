#!/usr/bin/env python3
def f1():
    print('f1 here')
x=f1
print('x=f1 and x gives f1 as object loc')
print(x)
print('Executing x=f1;x(); executes f1 contents ')
x();

