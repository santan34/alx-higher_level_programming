#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    x = set(filter(lambda y: y not in set_2, set_1))
    y = set(filter(lambda y: y not in set_1, set_2))
    a = x.union(y)
    return a
