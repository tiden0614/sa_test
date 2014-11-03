#!/usr/bin/python
#coding: utf-8

import sys

N = 15
factors = [6, 7]
multiples = []

def get_all_multiples():
    for f in factors:
        for i in xrange(0, N + 1):
            if i % f == 0:
                multiples.append(i)


get_all_multiples()
print multiples
