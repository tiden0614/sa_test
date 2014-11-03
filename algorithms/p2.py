#!/usr/bin/python
#coding: utf-8

import sys

N = 100
prime_marks = [0 for i in xrange(0, N + 1)]

def mark_primes():
    for i in xrange(2, N + 1):
        if prime_marks[i] == 0:
            for j in xrange(i + i, N + 1, i):
                prime_marks[j] = 1


def print_primes():
    for i, m in enumerate(prime_marks):
        if m == 0 and i > 1:
            print i,
    print ''

mark_primes()
print_primes()