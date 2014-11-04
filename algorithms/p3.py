#!/usr/bin/python
#coding: utf-8

import sys


def get_marker_map(input_str):
    marker = {}
    for c in input_str:
        if not marker.has_key(c):
            marker[c] = 1
        else:
            marker[c] += 1
    return marker


print get_marker_map('thisisanexample')