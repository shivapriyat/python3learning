#!/usr/bin/env python3
import time
def main():
    bigsum(1000000,'see string if passed')

def elapsed_time(f):
    def wrapper(limit,msg):
        startTime=time.time();
        f(limit,msg)
        endTime=time.time()
        print(f'time taken is: {(endTime-startTime)*1000} milliseconds')
    return wrapper

@elapsed_time
def bigsum(limit,msg):
    print(msg)
    numList=[]
    for i in range(limit):
        numList.append(i)
    print(f'big sum of list with element {limit} is {sum(numList)} ')


if __name__ == '__main__':main();