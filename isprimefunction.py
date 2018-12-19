#!/usr/bin/env python3
def isprime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
print('5 is prime {}'.format(isprime(5)))
print('15 is prime {}'.format(isprime(15)))
def listPrimes(max):
    for x in range(2,max):
        if(isprime(x)):
            print(x,end=' ',flush=True)
    print()

listPrimes(110)