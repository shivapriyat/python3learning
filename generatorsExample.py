#!/usr/bin/env python3

def main():
    print('range will always give 0 to 24, but we want inclusive range 0 to 25')
    for i in range(25):
        print(f'{i} ',end=' ',flush=True)
    print()
    print('Inclusive range function')
    for i in inclusive_range(25):
        print(f'{i} ',end=' ',flush=True)
    print()
    print('Inclusive range function start and stop from 1 to 10')
    for i in inclusive_range(1,10):
        print(f'{i} ', end=' ', flush=True)
    print()
    print('Inclusive range function start and stop from 5 to 25')
    for i in inclusive_range(0, 25,5):
        print(f'{i} ', end=' ', flush=True)
    print()
    print('Inclusive range with 0 args')
    for i in inclusive_range():
        print(f'{i} ', end=' ', flush=True)
    print()
    #error
    print('Inclusive range with 4 args')
    for i in inclusive_range(1,2,3,4):
        print(f'{i} ', end=' ', flush=True)
    print()


def inclusive_range(*args):
    numargs=len(args)
    start=0
    step=1

    if numargs<1:
        raise TypeError(f'expected atleast 1 arg but got {numargs}')
    elif numargs==1:
        stop=args[0]
    elif numargs==2:
        (start,stop)=args
    elif numargs==3:
        (start,stop,step)=args
    else:
        raise TypeError(f'expected atMOST 3 arg but got {numargs}')

#genaerator section
    i=start
    while(i<=stop):
        yield i     # continues to return all values
        i+=step


if __name__ == '__main__':main()
