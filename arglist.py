#!/usr/bin/env python3
def main():
    #multiple args
    print('Main with multiple args')
    printArgs('hello','world','hi','python',3)
    # empty args
    print('Main with empty args')
    printArgs()
    # list as args
    print('Main with list as args')
    list1=['shiva','priya']
    printArgs(*list1)

def printArgs(*args):
    if len(args):
        for s in args:
            print(f'\t {s}')
    else:
        print(f'\t empty args')

if __name__=='__main__':main()