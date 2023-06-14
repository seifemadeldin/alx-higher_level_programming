#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list(map(lambda x: x.replace(search, replace), my_list))
