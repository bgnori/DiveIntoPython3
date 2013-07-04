#!/usr/bin/python

def is_prime(n):
    ''' give n is prime or not. '''
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime(n):
    ''' make list of n primes '''
    xs = []
    i = 2
    while len(xs) < n:
        if is_prime(i):
            xs.append(i)
        i += 1
    return xs
