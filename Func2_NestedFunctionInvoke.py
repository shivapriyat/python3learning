#!/usr/bin/env python3

def f1():
    print('\t f1 start')

    def f2():
        print('\t\t f2 here')

    print('\t f1 ends here')
    return f2

x=f1;
print('main executing f1')
x();
print('main executing f2 through f1')
x()();
