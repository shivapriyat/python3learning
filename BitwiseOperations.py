#!/usr/bin/env/ python3
x=0x0a
y=0x02
z=x&y
print(f'hexadecimal bit and val is {x:02x} and {y:02x} is {z:02x}')
print(f'binary bit and val is {x:08b} and {y:08b} is {z:08b}')
print(f'decimal bit and val is {x} and {y} is {z}')
print()

z=x|y
print(f'hexadecimal bit OR val is {x:02x} and {y:02x} is {z:02x}')
print(f'binary bit OR val is {x:08b} and {y:08b} is {z:08b}')
print(f'decimal bit OR val is {x} and {y} is {z}')
print()

z=x^y
print(f'hexadecimal bit XOR val is {x:02x} and {y:02x} is {z:02x}')
print(f'binary bit XOR val is {x:08b} and {y:08b} is {z:08b}')
print(f'decimal bit XOR val is {x} and {y} is {z}')
print()

y=1
z=x<<y
print(f'hexadecimal bit LS val is {x:02x} and {y:02x} is {z:02x}')
print(f'binary bit LS val is {x:08b} and {y:08b} is {z:08b}')
print(f'decimal bit LS val is {x} and {y} is {z}')

z=x>>y
print(f'hexadecimal bit RS val is {x:02x} and {y:02x} is {z:02x}')
print(f'binary bit  RS is {x:08b} and {y:08b} is {z:08b}')
print(f'decimal bit RS is {x} and {y} is {z}')