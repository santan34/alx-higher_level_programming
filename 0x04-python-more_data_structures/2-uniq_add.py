#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    my_list = set(my_list)
    for i in my_list:
        sums = sums + i
    return sums
