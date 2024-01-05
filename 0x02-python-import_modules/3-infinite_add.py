#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        sum = 0
    else:
        for i in range(len(sys.argv)):
            if i == 0:
                sum = 0
            else:
                sum = sum+int(sys.argv[i])
    print("{}".format(sum))
