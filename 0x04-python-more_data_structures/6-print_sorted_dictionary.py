#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for i in new_dic:
        print("{}: {}".format(i, new_dic[i]))
