#! /usr/bin/python3

# Valid:

a, b, c = 1, 2, 3
d,*e = 1, 2, 3, 4
[d,*e] = 1, 2, 3, 4

# Invalid:

a, b, c = 1, 2
a, b, c = 1, [2, 3]