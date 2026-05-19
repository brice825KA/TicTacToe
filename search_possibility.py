#! /usr/bin/env python3


def valid_list(ligne):
    first = ligne[0]
    letter = [True, first]
    for char in ligne:
        if char != first:
            letter[0] = False
            return letter
    return letter


def horizontal(matrix, size):
    newmatrix = []
    for i in matrix:
        newmatrix.append(i)
    return newmatrix


def vertical(matrix, size):
    newmatrix = []

    for i in range(size):
        lab = []
        for j in range(size):
            lab.append(matrix[j][i])
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
    return diagonal


def learn_possibility(matrix, size, table_char):
    table = []
    answer = True
    table.append(horizontal(matrix, size))
    table.append(vertical(matrix, size))
    table.append(diagonal(matrix, size))

    print(f"{table}")
    for box in table:
        for ligne in box:
            answer = valid_list(ligne)
            if answer[0] == "True":
                print(f"le vainceur est {answer[1]}")
                exit(0)
            else:
                continue
    return 0
