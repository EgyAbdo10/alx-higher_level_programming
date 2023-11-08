#!/usr/bin/python3
"""Create Pascal's Triangle"""

def my_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def comb_list(n):
    if n < 0:
        return []
    m = n
    comb_list = []
    for m in range(n + 1):
        val = my_factorial(n) // (my_factorial(n - m) * my_factorial(m))
        comb_list.append(val)
    return comb_list

def pascal_triangle(n):
    if n <= 0:
        return []
    pascal_2d_list = []
    for i in range(n):
        pascal_2d_list.append(comb_list(i))
    return pascal_2d_list

