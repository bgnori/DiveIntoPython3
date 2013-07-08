#!/usr/bin/python

def foo(n):
    '''
    5) Fizz Buzzのリストxsを内包表記を用いてつくる関数foo(n)を実装せよ.
    0 < n
    xs[1] = 1, xs[2] = 2, xs[3] ='Fizz', 
    ... xs[15] = 'Fizz Buzz' ... xs[n] = ??? などとなる.
    '''
    return ['Fizz Buzz' if x % (3*5) == 0 else 'Fizz' if x % 3 == 0 else
            'Buzz' if x % 5 == 0 else x for x in range(n+1)]
