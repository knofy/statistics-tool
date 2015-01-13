#!/usr/bin/env python3

"""
Module for performing various statistical operations
"""

import math
import scipy
import numpy


def items(filename):
    """Return one line at a time as dictionary.

    The first line has to be a header that can be used as dictionary keys. All
    numeric values in the input file are automatically converted to float.
    Calling this generator function again after the last line restarts at the
    top.
    """
    with open(filename, encoding='utf-8-sig') as f:
        header = [e.strip() for e in f.readline().split(',')]
        for line in f:
            if not line.strip():
                continue
            columns = line.split(',')
            item = dict(zip(header, columns))
            for key in item:
                try:
                    item[key] = float(item[key])
                except:
                    pass
            yield item


def count(filename):
    """Return the number of items in the given file."""
    num_items = 0
    for item in items(filename):
        num_items += 1
    return num_items


def calc_mean(filename, key):
    """
    Calculates the Mean of the Fileinput of the given Key.
    """

    sum_of_values = 0
    for item in items(filename):
        sum_of_values += item[key]
    return sum_of_values / count(filename)


def calc_stddev(filename, key):
    """
    Calculates the Standarddeviation of the Fileinput of the given Key.
    """

    a = []
    for item in items(filename):
        a.append(item[key])
    return scipy.std(a)


def calc_sum(filename, key):
    """
    Calculates the Sum of the Fileinput of the given Key.
    """

    sum_of_values = 0
    for item in items(filename):
        sum_of_values += item[key]
    return sum_of_values


def calc_variance(filename, key):
    """
    Calculates the Variance of the Fileinput of the given Key.
    """

    a = []
    for item in items(filename):
        a.append(item[key])
    return scipy.var(a)


def find_max(filename, key):
    """
    Finds the Maximum of the Fileinput of the given Key.
    """
    
    a = []
    for item in items(filename):
        a.append(item[key])
    return numpy.max(a)


def find_min(filename, key):
    """
    Finds the Minumum of the Fileinput of the given Key.
    """
    
    a = []
    for item in items(filename):
        a.append(item[key])
    return numpy.min(a)