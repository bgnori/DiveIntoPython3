#!/usr/bin/python

def wordcount(xs):
    '''simple implementation of wordcount.
    using collections.Counter is also good idea.

    "d.get(x, 0)" is the pattern should be learned.
    '''
    d = {}
    for x in xs:
        c = d.get(x, 0) + 1
        d[x] = c
    return d
