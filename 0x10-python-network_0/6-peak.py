#!/usr/bin/python3
"""this module is used to find the peak of a list of some numbers"""


def find_peak(list_of_integers):
    """find the peak of a list of numbers"""
    temp = list_of_integers[0]
    for i in range(len(list_of_integers)):
        if i < (len(list_of_integers) - 1) and list_of_integers[i + 1] > temp:
            temp = list_of_integers[i + 1]
    return temp
