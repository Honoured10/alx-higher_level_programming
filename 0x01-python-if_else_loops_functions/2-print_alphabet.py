#!/usr/bin/python3
letter = range(ord('a'), ord('z')+1)
for i in letter:
    print('{:c}'.format(i), end="")
