#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            string = string + i
        else:
            string = string + i
    print("{}".format(string))
