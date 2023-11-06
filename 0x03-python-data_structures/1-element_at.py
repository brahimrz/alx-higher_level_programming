#!/usr/bin/python3
def element_at(my_list, idxx):
    if idxx < 0 or idxx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idxx]
