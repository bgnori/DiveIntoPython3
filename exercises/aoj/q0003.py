#!/usr/bin/python

def reader(f):
    ''' '''
    xxs = []
    for i, line in enumerate(f):
        if i == 0:
            continue
        xs = list(map(int, line.split()))[1:]
        xxs.append(xs)
    return xxs

