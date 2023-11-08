# !/usr/bin/python3
"""create the pascal triangle"""


def my_factorial(n):
    """get the factorial of a number"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * my_factorial(n - 1)


def comb_list(n):
    """get a list of all the numbers of combinations
    nCm from m = 0 to m = n"""
    if n < 0:
        return []
    m = n
    comb_list = []
    while (m >= 0):
        val = int((my_factorial(n) / my_factorial(n - m)) / my_factorial(m))
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
