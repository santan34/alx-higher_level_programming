#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            nw.append(replace)
        else:
            nw.append(my_list[i])
    return nw
