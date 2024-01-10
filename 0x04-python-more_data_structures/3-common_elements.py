#!/usr/bin/python3
def common_elements(set_1, set_2):
    x = set(filter(lambda y: y in set_2, set_1))
    return x
