#!/usr/bin/python
#coding: utf-8

#Usage: python p4.py 10000

import sys

N = 500
a = [5, 10, 20, 50, 100, 200]

def f(i, j):
    if j == 0:
        return 1
    if i == 0:
        return 0
    if store_matrix[i - 1][j] != -1:
        return store_matrix[i - 1][j]
    sum, w = 0, a[i - 1]
    for W in xrange(0, j + 1, w):
        if j - W < 0:
            break
        sum += f(i - 1, j - W)
    store_matrix[i - 1][j] = sum
    return sum


if '__main__' == __name__:
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    store_matrix = [[-1 for n in xrange(N + 1)] for m in xrange(len(a))]
    print f(len(a), N) % 1000000