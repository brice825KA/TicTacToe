#! /usr/bin/env python3

import math
import sys

from usage import usage
from search_possibility import learn_possibility


def print_matrix(matrix, size):
    for ligne in matrix:
        print(ligne)


def cout_matrix(matrix, size):
    cout = 0
    for ligne in matrix:
        for row in ligne:
            if row == 0:
                cout += 1
    return cout


def set_game(matrix, table_char, size):
    while 1:
        pose = []
        pose = input().split(" ")
        if len(pose) != 2:
            continue
        if len(pose[0]) != 1 or len(pose[1]) != 1:
            continue
        elif pose[0].isalpha() != 1 or pose[1].isdigit() != 1:
            continue
        else:
            if int(pose[1]) > math.pow(size, 2):
                print("Position invalid")
                continue
            elif pose[0] != table_char[0] and pose[0] != table_char[1]:
                print("Char invalid")
                continue
            else:
                if matrix[(int(pose[1]) - 1) // size][int(pose[1]) % size] != 0:
                    print("Position invalid")
                    continue
                else:
                    matrix[(int(pose[1]) - 1) // size][int(pose[1]) % size] = pose[0]
                    learn_possibility(matrix, size, table_char)
                    print_matrix(matrix, size)


def create_table_game(size):
    matrix = []
    for i in range(size):
        new_table = [0] * size
        matrix.append(new_table)
    return matrix


def main():
    table_char = []

    if len(sys.argv) != 2:
        sys.exit(84)
    if sys.argv[1] == "-h":
        usage()
        sys.exit(0)
    matrix_gamer = create_table_game(int(sys.argv[1]))
    for row in matrix_gamer:
        print(row)
    table_char = input().split(" ")
    if len(table_char) != 2:
        sys.exit(84)
    print(table_char)
    set_game(matrix_gamer, table_char, int(sys.argv[1]))


if __name__ == "__main__":
    main()
