#!/usr/bin/python

def deffind(f):
    ''' returns list of lines, start with def'''
    return [line for line in f if line.startswith('def')]

