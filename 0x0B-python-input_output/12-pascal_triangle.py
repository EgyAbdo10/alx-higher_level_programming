#!/usr/bin/python3
"""create the pascal triangle"""


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def comb_list(n):
    """get all the numbers of combinations
    nCm from m = 0 to m = n"""
    if n < 0:
        return []
    m = n
    comb_list = []
    while (m >= 0):
        val = int((factorial(n) / factorial(n - m)) / factorial(m))
        comb_list.append(val)
        m -= 1
    return comb_list


def pascal_triangle(n):
    """draw pascal triange of height n lists"""
    if n <= 0:
        return []
    else:
        pascal_2d_list = []
        i = 0
        while (i < n):
            pascal_2d_list.append(comb_list(i))
            i += 1
        return pascal_2d_list
