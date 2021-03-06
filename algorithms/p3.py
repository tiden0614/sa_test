#!/usr/bin/python
#coding: utf-8

#This script prints the reversed order of a given string
#For easy implementation, it employs the insertion sort algorithm, of which the time complexity is O(n^2)
#It could be improved using quick sort or merge sort
#However in a interview test, time is limited for testing the more complicated algorithms

import sys


def get_marker_map(input_str):
    marker = {}
    for c in input_str:
        if not marker.has_key(c):
            marker[c] = 1
        else:
            marker[c] += 1
    return marker



def print_reversed_str(input_str):
    marker = get_marker_map(input_str)
    out_array = []
    for k, v in marker.items():
        if len(out_array) == 0:
            out_array.insert(0, k)
        else:
            i = 0
            while i < len(out_array) and ord(out_array[i]) >= ord(k):
                i += 1
            out_array.insert(i, k)

    print ''.join([c * marker[c] for c in out_array])


if '__main__' == __name__:
    input_str = 'thisisanexample'
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    print_reversed_str(input_str)
