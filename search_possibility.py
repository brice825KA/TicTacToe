#! /usr/bin/env python3


def valid_list(ligne):
    first = ligne[0]
    for char in ligne:
        if char != first:
            return False
    return True


def horizontal(matrix, size):
    newmatrix = []
    answer = True
    for i in matrix:
        newmatrix.append(i)
        answer = valid_list(i)
        if answer == True:
            print(f"Winner is {i[0]}")
    return newmatrix


def vertical(matrix, size):
    newmatrix = []

    for i in range(size):
        lab = []
        for j in range(size):
            lab.append(matrix[j][i])
        newmatrix.append(lab)
        answer = valid_list(lab)
        if answer == True:
            print(f"Winner is {lab[0]}")
    return newmatrix


def diagonal(matrix, size):
    diagonal = []
    diagone = []
    diagtwo = []
    for i in range(size):
        diagone.append(matrix[i][i])
        diagtwo.append(matrix[i][size - 1 - i])
    diagonal.append(diagone)
    diagonal.append(diagtwo)
    for ligne in diagonal:
        answer = valid_list(ligne)
        if answer == True:
            print(f"Winner is {ligne[0]}")
    return diagonal


def learn_possibility(matrix, size, table_char):
    horizontal(matrix, size)
    vertical(matrix, size)
    diagonal(matrix, size)
