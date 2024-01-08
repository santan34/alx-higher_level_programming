#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw = []
    for i in my_list:
        if i % 2 == 0:
            nw.append(True)
        else:
            nw.append(False)
    return nw
