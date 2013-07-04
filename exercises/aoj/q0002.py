#!/usr/bin/python

def colonfind(f):
    ''' returns list of lines, end with ):'''
    return [line for line in f if line.endswith('):\n')]
