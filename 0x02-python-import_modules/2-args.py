#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l > 2:
        string = "arguments:"
    elif l == 1:
        string = "arguments."
    else:
        string = "argument:"
    for i in range(l):
        if i == 0:
            print("{} {}".format(l-1, string))
        else:
            print("{}: {}".format(i, sys.argv[i]))
