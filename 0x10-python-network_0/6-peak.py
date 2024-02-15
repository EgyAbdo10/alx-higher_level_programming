#!/usr/bin/python3
"""this module is used to find the peak of a list of some numbers"""


def find_peak(list_of_integers):
    """find the peak of a list of numbers"""
    if len(list_of_integers) == 0:
        return None

    first_idx, last_idx = 0, len(list_of_integers) - 1
    mid = list_of_integers[(first_idx + last_idx) // 2]
    while first_idx < last_idx:
        mid_idx = (first_idx + last_idx) // 2
        mid = list_of_integers[mid_idx]
        after = list_of_integers[mid_idx + 1]
        if mid > after and (mid_idx == 0 or
                            mid > list_of_integers[mid_idx - 1]):
            return mid
        elif mid < after:
            first_idx = mid_idx + 1
        elif mid < list_of_integers[mid_idx - 1]:
            last_idx = mid_idx - 1
        elif mid == after:
            last_idx = mid_idx - 1
        elif mid == list_of_integers[mid_idx - 1]:
            first_idx = mid_idx + 1

    return list_of_integers[first_idx]
