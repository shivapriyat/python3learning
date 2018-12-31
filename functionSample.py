#!/usr/bin/env python3
def main():
    dog()
    x=dogcount(5)
    print(x)
    legCount=doglegs();
    print(legCount)
def dog():
    print('Bow bow')
def dogcount(n) :
    print(f'{n} saying bow bow')
def doglegs():
    return 4
if __name__=='__main__' : main();