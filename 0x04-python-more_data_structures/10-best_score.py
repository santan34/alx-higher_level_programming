#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    name = ""
    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if a < a_dictionary[i]:
            a = a_dictionary[i]
            name = i
    return name
