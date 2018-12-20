#!/usr/bin/env python3
#multi line string
x='''
seven
eight
'''
print(x)
#capitalize string
y='seven'
print('case capitalize {}'.format(y.capitalize()))
#uppercase
print('case:upper: {}'.format('seven'.upper()))
#lowercase
print('case:lower: {}'.format('Seven'.lower()))
#format is positional substituter
print('case:format:  seven {} {}'.format(8,9))
#format is positional substituter and use index to print
print('case:substitute based on index:  seven {1} {0}'.format(8,9))
#format more args   --- no impact
print('case:more args:  seven {} {}'.format(8,9,10))

#left align and right align values
print('seven "{1:<4}" "{0:>4}"'.format(8,9))
#inside quotes print values
a=3
b=4
print(f'{a} {b}')
#format more placeholders --- index error and exit
print('case:more placeholder:  seven {} {} {}'.format(8,9))