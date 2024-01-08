#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nl = []
    for i in my_list:
        nl.append(i)
    if idx < 0:
        return nl
    if idx > len(my_list)-1:
        return nl
    nl[idx] = element
    return nl
