#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    NewArr = []
    for i in range(matrix):
        for j in range(matrix):
            NewArr.append(matrix[i,j]**2)[i,j]
    return NewArr