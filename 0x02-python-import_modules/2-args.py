#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l > 1:
        string = "arguments"
    else:
        string = "argument"
    for i in range(l):
        if i == 0:
            print("{} {}:".format(l, string))
        else:
            print("{}: {}".format(i, sys.argv[i]))
