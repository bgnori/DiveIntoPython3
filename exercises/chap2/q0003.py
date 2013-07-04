#!/usr/bin/python


def fizzbuzz(n):
    '''Fizz Buzz'''
    if n % 15 == 0:
        return "Fizz Buzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

def fizzbuzz_t(n):
    '''tuple of Fizz Buzz seq'''
    xs = []
    for i in range(n):
        xs.append(fizzbuzz(i))
    return tuple(xs)
