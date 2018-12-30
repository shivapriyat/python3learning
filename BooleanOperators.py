#!/usr/bin/env python3

a=True
b=False
x=('apple','mango','banana','grape')
y='mango'
z='orange'
if a and b:
    print('a and b result is True')
else :
    print('a and b result is False')

if a or b:
    print('a or b result is True')
else :
    print('a or b result is False')

if not b:
    print(' not b is True ')
else:
    print('not b is true')
# in operator
if y in x:
    print('y is a value in x arr')
else:
    print('y is not found in x arr')

# in operator
if z in x:
    print('z is a value in x arr')
else:
    print('z is not found in x arr')

# is with index operator
if y is x[1]:
    print('y is a element x arr and id of y {} and id of x[1] {}',id(y),id(x[1]))
else:
    print('y is not  element x arr')

# is with index operator
if y is not x[1]:
    print('y is not an element x arr and id of y and id of x[1]')
else:
    print('y is an  element x arr')