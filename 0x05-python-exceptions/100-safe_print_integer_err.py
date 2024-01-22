#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        import sys
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as msf:
        sys.stderr.write("Exception: {}\n".format(msf))
        return False
