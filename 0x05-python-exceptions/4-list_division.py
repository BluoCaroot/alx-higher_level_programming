#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            c = "divsion by 0"
            x = 0
            print(c)
        except TypeError:
            c = "wrong type"
            x = 0
            print(c)
        except IndexError:
            c = "out of range"
            x = 0
            print(c)
        finally:
            ret.append(x)
    return (ret)
