#!/usr/bin/env python3
mytuple=(1,2,3,4)
print('mytuple=(1,2,3,4) type={}'.format(type(mytuple)))

mytupleCombo=(1,'two',3.0,[4,'FOUR'],5)
print('mytupleCombo=(1,"two",3.0,[4,"FOUR"],5)   type {}'.format(type(mytupleCombo)))
print('mytupleCombo[3]  type{}'.format(type(mytupleCombo[3])))

#id unique identifier of each object
print('mytuple id {}'.format(id(mytuple)))
print('mytupleCombo id {}'.format(id(mytupleCombo)))

#id of same literals are equal
print('mytuple[0] id {}'.format(id(mytuple[0])))
print('mytupleCombo[0] id {}'.format(id(mytupleCombo[0])))

#is compare 2 objects in tuples with their values provided they are primitive
if mytuple[0] is mytupleCombo[0]:
    print('mytuple[0] is mytupleCombo[0]')
else:
    print('mytuple[0] nNOT mytupleCombo[0]')

mytupleCombo1=(1,'two',3.0,[4,'FOUR'],5)
# is fails for objects equal which has nested objects:
if mytupleCombo is mytupleCombo1:
    print('mytupleCombo is mytupleCombo1 2 complex objs are equal')
else:
    print('mytupleCombo is mytupleCombo1 2 complex objs are NOTTTTT  equal')

# instanceof in java = isInstance(x,int)
if(isinstance(mytupleCombo,tuple)):
    print('mytupleCombo is instance of tuple')
else:
    print('mytupleCombo is NOTTTT instance of tuple')

mylist=[1,"2",3.0]
if(isinstance(mylist,tuple)):
    print('mylist is tuple')
elif(isinstance(mylist,list)):
    print('mylist is list')
else:
    print('else mylist is {}'.format(type(mylist)))
