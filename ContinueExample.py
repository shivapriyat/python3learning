#!/usr/bin/env python3
fruits=('apple','mango','banana','grape')
for fruit in fruits :
    if fruit=='mango':
        continue
    print(fruit)
else:
    print('ended for loop in normal way')