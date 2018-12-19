#!/usr/bin/env python3
#default value when arg is not passed
def function(n=1):
    print(n)
function(47)
function()
#  default return value is NONE
def function2(n):
    print(n)
x=function2(12)
print(x)

#with return statement
def function3(n):
    print(n)
    return n*2
x=function3(6)
print(x)