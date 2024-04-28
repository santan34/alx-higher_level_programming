#!/usr/bin/python3
"""
find the peak of a list
"""


def peaky(low, high, lists):
    """
    recursie function to find the peak
    """
    mid = (low + high) // 2
    if low == high:
        return lists[low]
    if lists[mid] < lists[mid + 1]:
        return peaky(mid + 1, high, lists)
    return peaky(low, mid, lists)


def find_peak(list_of_integers):
    """the required function"""
    if not list_of_integers:
        return
    return peaky(0, len(list_of_integers) - 1, list_of_integers)
