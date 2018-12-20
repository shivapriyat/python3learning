#!/usr/bin/env python3
#to solve precision problem over accuracu use Decimal from decimal package
from decimal import *
a=Decimal('0.1')
b=Decimal('0.3')
c=a+a+a-b
print('c is {} and type {}'.format(c,type(c)))