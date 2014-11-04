#!/usr/bin/python
#coding: utf-8

import sys

N = 2000
factors = [6, 7]
multiples = []

def get_all_multiples():
    for f in factors:
        for i in xrange(1, N + 1):
            if i % f == 0:
                multiples.append(i)


if '__main__' == __name__:
    if len(sys.argv) > 1:
        N = sys.argv[1]
    get_all_multiples()
    print sum(multiples)