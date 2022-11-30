#!/usr/bin/python3
letter = range(ord('a'), ord('z')+1)
for i in letter:
    if i == ord('e') or i == ord('q'):
        continue
    print('{:c}'.format(i), end='')
    