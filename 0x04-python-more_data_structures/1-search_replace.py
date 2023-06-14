#!/usr/bin/python3

def search_replace(my_list, search, replace):
    indx = lists.index(search)
    lists = my_list[:indx]+[replace]+lists[indx+1:]
    return(lists)
