#!/usr/bin/env python3

def main():
    #multiple args
    kitten(5,6,7)
    #making last arguments optional
    kittenDefaultArgs(1,2)
    kittenDefaultArgs(1, 2,3)
    # integer is callby value
    x=5
    callbyvalue(x)
    print(f'in main call by value integer passed:{x}')
    #list follows call by reference
    list1=[5,1,2]
    list2=list1
    list2[0]=3
    print(f'call by ref id(list1) : {id(list1)}')
    print(f'call by ref id(list2) : {id(list2)}')
    print(f'call by ref (list1) : {list1}')
    print(f'call by ref (list2) : {list2}')
def kitten(a,b,c):
    print('Meow')
    print(a,b,c)

def kittenDefaultArgs(a,b,c=0):
    print('Meow')
    print(a,b,c)

def callbyvalue(a):
    a=3
    print(f'callbyvalue:{a} ')

if __name__=='__main__': main()