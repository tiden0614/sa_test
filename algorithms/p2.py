#!/usr/bin/python
#coding: utf-8

import sys

n = 1500000

def mark_primes(N):
    prime_marks = [0 for i in xrange(0, N + 1)]
    for i in xrange(2, N + 1):
        if prime_marks[i] == 0:
            for j in xrange(i + i, N + 1, i):
                prime_marks[j] = 1
    return prime_marks


def get_primes(prime_marks):
    primes = []
    for i, m in enumerate(prime_marks):
        if m == 0 and i > 1:
            primes.append(i)
    return primes


if '__main__' == __name__:
    if len(sys.argv) > 1:
        n = int(sys.argv)
    print sum(get_primes(mark_primes(n)))