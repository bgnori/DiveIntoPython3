#!/usr/bin/python

def flatten(xs):
    ''' assume that xs and its items do not reference itself'''
    
    r = []
    for x in xs:
        if isinstance(x, list):
            r.extend(flatten(x))
        else:
            r.append(x)
    return r
