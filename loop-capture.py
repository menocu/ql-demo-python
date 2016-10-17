#! /usr/bin/python2

funcs = [lambda: a * 2 for a in range(3)]

# Expected: [0, 2, 4]
# Actual: [4, 4, 4]
print [f() for f in funcs]

