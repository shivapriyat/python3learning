#!/usr/bin/env python3
def main():
    x=noreturn()
    print(f'type: {type(x)} and value: {x}')
    y=intreturn()
    print(f'type: {type(y)} and value: {y}')
    z=listreturn()
    print(f'type: {type(z)} and value: {z}')
    a=dictreturn()
    print(f'type: {type(a)} and value: {a}')

def noreturn():
    a=1
def intreturn():
    return 42
def listreturn():
    return [1,2,3]
def dictreturn():
    return dict(one=1,two=2,three=3)

if __name__=='__main__':main()