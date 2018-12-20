#!/usr/bin/env python3

def function(x):
    if x==1:
        return 'if x==1'
    elif x==2:
        return 'elif x==2'
    elif x==3:
        return 'elif x==3'
    elif x==4:
        return 'elif x==4'
    elif x==5:
        return 'elif x==5'
    else:
        return 'none of values match'

def main():
    print(function(1))
    print(function(3))
    print(function(11))

if __name__=='__main__':main()