#!/usr/bin/env python3

def f1(f):
    print('\t f1 start here')
    def f2():
        print('\t\t f2 start here')
        f()
        print('\t\t f2 end here')
    return f2

def f3():
    print('\t\t\t f3 here')

x=f1(f3)
x()
