"""
the string "ABC" in binary is:
2^x   7654 3210
A: 0b 0100 0001
B: 0b 0100 0010
C: 0b 0100 0011
together:
0b | 0100 0001 | 0100 0010 | 0100 0011
or without spaces
0b010000010100001001000011
to convert it to base 64 (which is 2^6) we need to split
binary representation by 6 bits instead of 8 (as above)
0b | 010000 | 010100 | 001001 | 000011

Now we need 64 characters to represent 64-base, let's choose a set
{A-Z, a-z, 0-9, +, /}
A:000000 = 0
B:000001 = 1
C:000010 = 2
D:000011 = 3
...
Q:010000 = 16
...
/:111111 = 63

total is 64 chars
last letter: 000011 is 3 in decimal, which is 4th in order (=D)
the whole encoded string is then: QUJD

If the total number bits is not divisible by 6, say "A", ord('A') = 65
binary 0b 0100 0001
converting to 6 bits, 8 not divisible by 6, neither 16, but 24 is, so
adding padding for a total of 24 bits
0b 0100 0001 | 0000 0000 | 0000 0000
now we can regroup by 6
 0b 010000|010000|------|------
2^x 543210 543210 543210 543210
 0b 010000|010000|------|------
the last two characters (resulting for padding) replaced with "="
2^4 = 16, so 010000 = 16 which is 17th letter which is Q, so we have
QQ==
"""

import base64


print("\nExample with perfect match")
s = b"ABC"
print("Original {}".format(s))
b = base64.standard_b64encode(s)
print("base64 encoded {}".format(b))
d = base64.standard_b64decode(b)
print("base64 decoded {}".format(d))

print("\nExample with padding")
s = b"A"
print("Original {}".format(s))
b = base64.standard_b64encode(s)
print("base64 encoded {}".format(b))
d = base64.standard_b64decode(b)
print("base64 decoded {}".format(d))
