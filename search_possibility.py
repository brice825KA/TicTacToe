#! /usr/bin/env python3

def valid_list(ligne):
    first = ligne[0]
    for char in ligne:
        if char != first:
            return False
    return True

def horyzontal(matrix, size):
    newmatrix = []
    for i in matrix:
        newmatrix.append(i)
    return newmatrix

def vertical(matrix, size):
    newmatrix = []
    i, j = 0, 0
    const_i = 0

    while i < size:
        lab = []
        const_i = i
        for  j in range(size):
            lab.append(matrix[i][j])
            i += 1
        i = const_i
    return newmatrix

def diagonal(matrix, size):
    diagonal = []
    for i in range(size):
        lab = []
        for j in range(size):
            if i == j:
                lab.append(matrix[i][j])
        diagonal.append(lab)

    for row in range(size, 0, -1):
        lab = []
        for col in range(size, 0, -1):
            if  row + col == size:
                lab.append(matrix[row][col])
        diagonal.append(lab)
    return diagonal

def learn_possibility(matrix, size, table_char):
    return 0

