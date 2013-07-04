#!/usr/bin/python

def reader(f):
    ''' '''
    xxs = []
    for i, line in enumerate(f):
        xs = list(map(int, line.split()))
        if len(xs) == 1 and xs[0] == 0:
            break
        xxs.append(xs)
    return xxs

