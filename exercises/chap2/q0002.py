#!/usr/bin/python


def fizzbuff(n):
    '''Fizz Buzz'''
    if n % 15 == 0:
        return "Fizz Buzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n
