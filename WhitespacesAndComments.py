#!/usr/bin/env python3
import platform
def main():
    message()

def message():
    print('message line1')
    if True:
        print('if true block')
    else:
        print('else true block not seen')
    if False:
        print('if false block not seen')
    else:
        print('else false block')
if __name__=='__main__':main()