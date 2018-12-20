#!/usr/bin/env python3
values=[1,2,3,4,5]
for i in values:
    print('i is {}'.format(i),end=' ',flush=True)
print()
values[2]=11
for i in values:
    print('i is {}'.format(i),end=' ',flush=True)
print()
#tuple is immutable, sequence is mutable
values=(1,2,3,4,5)
print('tuple values=(1,2,3,4,5) immutable')
for i in values:
    print('{}'.format(i),end=' ',flush=True)
print()
# range values
x=range(5)
print('range is immutable 5 ')
for i in x:
    print('{}'.format(i),end=' ',flush=True)
print()
x=range(5,10)
print('start and stop range 5,10 ')
for i in x:
    print('{}'.format(i),end=' ',flush=True)
print()
x=range(5,50,7)
print('start stop step by range 5,50,7')
for i in x:
    print('{}'.format(i),end=' ',flush=True)
print()
#construct mutable range
mylist=list(range(5))
print('list of range is mutable:')
mylist[1]=15
for i in mylist:
    print(i,end=' ',flush=True)
print()
#Dictonary - searchable  key value paits and immutable
mydictionary={'one':1,'two':2,'three':3,'four':4,'five':5}
mydictionary['four']='FOUR'
for k,v in mydictionary.items():
    print('key:{} and value:{}'.format(k,v))