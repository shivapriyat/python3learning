#!/usr/bin/env python3

name='priya'
inputname=''
count=0;
max_count=5
auth=False

while name!=inputname:
    count+=1
    if count>max_count:
        break
    inputname=input(f'{count} enter your name:  ')
else:
    auth=True
print('authorized' if auth else 'login failed')