#!/usr/bin/env python3
x=42
y=73
if x<y:
    print('x<y value of x is: {} and y ={}'.format(x,y))

#if without blocks for single statement
if x<y:print('x<y value of x is: {} and y ={}'.format(x,y))
#else sample
if x>y:
    print('x<y value of x is: {} and y ={}'.format(x, y))
else:
    print('else block x<y value of x is: {} and y ={}'.format(x, y))
#else if example
if x>y:
    print('if x>y')
elif x<y:
    print('elif x<y')
else:
    print('else x==y')