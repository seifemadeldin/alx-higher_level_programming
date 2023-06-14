#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    NewArr = []
    for i in matrix:
        for j in matrix:
            NewArr[i,j] = matrix[i,j]**2
    return NewArr