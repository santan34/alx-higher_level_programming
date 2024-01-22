#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    try:
        for i in range(list_length):
            try:
                x = my_list_1[i]/my_list_2[i]
                ls.append(x)
            except ZeroDivisionError:
                print("division by 0")
                ls.append(0)
            except (ValueError, TypeError):
                print("wrong type")
                ls.append(0)
    except IndexError:
        print("out of range")
    finally:
        return ls
